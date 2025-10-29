from collections import defaultdict
import re
import unicodedata
import os

MODULE_DIR = os.path.dirname(__file__)

__all__ = ['convert', 'CORE', 'ALL', 'J', 'K', 'T', 'NOT_UNIFIABLE', 'AD', 'MO', 'MS']

CORE = 'c'
ALL = '*'

J = 'j'
K = 'k'
T = 't'

IVS_COMP_CLASH = "'"

ALTERNATE = 'v'
ETYMOLOGICAL = 'a'

TIAO_NA = '\\'

REVERSE = '<'

NOT_UNIFIABLE = 'n'

AD = 'ad'
MO = 'mo'
MS = 'ms'

CENTERABLE_PUNCTATION = '、。！，．：；？'

def read_tsv(filename):
    returned = {}
    
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            key_value = line.rstrip('\n').split('\t')
            
            key = key_value[0]
            value = key_value[1]
            
            returned[key] = value
    
    return returned

def read_ivs_table(filename):
    returned = {}
    
    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            key_value = line.rstrip('\n').split('\t')
            
            key = key_value[0]
            value = key_value[1]
            attr = key_value[2] if len(key_value) >= 3 else ''
            
            returned[key] = value, attr
    
    return returned

def is_cjk(char):
    ord_ = ord(char)
    return (0x3400 <= ord_ <= 0x4dbf) or (0x4e00 <= ord_ <= 0x9fff) or (0xf900 <= ord_ <= 0xfaff) or (0x20000 <= ord_ <= 0x323af)

with open(os.path.join(MODULE_DIR, 'conversion-tables/variants_list.txt'), 'rt', encoding='utf-8') as file:
    VARIANTS_TABLE = {}
    J_TABLE = {}
    K_TABLE = {}
    T_TABLE = {}
    
    SUPP_CORE_LIST = set()
    
    for line in file:
        key_value = line.rstrip('\n').split('\t')
        key = key_value[0]
        value = key_value[1]
        
        if len(key_value) >= 3:
            attr = key_value[2]
        else:
            attr = ''
        
        remove_locale_tag = lambda attr: re.sub('[jkt]', '', attr)
        
        no_attr = True
        
        if J in attr:
            J_TABLE[key] = value, remove_locale_tag(attr)
            no_attr = False
        if K in attr:
            K_TABLE[key] = value, remove_locale_tag(attr)
            no_attr = False
        if T in attr:
            T_TABLE[key] = value, remove_locale_tag(attr)
            no_attr = False
        
        if no_attr:
            VARIANTS_TABLE[key] = value, attr
            
        if CORE in attr:
            SUPP_CORE_LIST.add(value)

COMPATIBILITY_CORRECTED_MAPPING = read_tsv(os.path.join(MODULE_DIR, 'conversion-tables/compatibility_corrected_mapping.txt'))

IVS_AD_TABLE = read_ivs_table(os.path.join(MODULE_DIR, 'conversion-tables/ivs-adobe-japan1.txt'))
IVS_MO_TABLE = None # read_ivs_table(os.path.join(MODULE_DIR, 'conversion-tables/ivs-moji-joho.txt'))
IVS_MS_TABLE = read_ivs_table(os.path.join(MODULE_DIR, 'conversion-tables/ivs-mscs.txt'))

def convert(string: str, *, supp_planes=CORE, compatibility=[J, K, T], convert_not_unifiable=True, alternate=False, etymological=False, ivs=False, tiao_na=True, punctation_align_center=False) -> str:
    if not ivs and tiao_na:
        tiao_na = False
    
    if not supp_planes:
        supp_planes = ''
    
    if supp_planes not in {'', CORE, ALL}:
        raise TypeError
    
    if compatibility:
        map_ = lambda x: {J: J_TABLE, K: K_TABLE, T: T_TABLE}[x]
        compatibility_tables_ordered = [map_(i) for i in compatibility]
    else:
        compatibility_tables_ordered = []
        compatibility = []
    
    if ivs:
        if 'mo' in ivs:
            raise NotImplementedError('Moji-Joho IVS conversion is temporarily removed due to inadequate conversion table')
            
        map_ = lambda x: {AD: IVS_AD_TABLE, MO: IVS_MO_TABLE, MS: IVS_MS_TABLE}[x]
        ivs_tables_ordered = [map_(i) for i in ivs]
    else:
        ivs_tables_ordered = []
    
    # remove existing variation selectors and normalize compatibility ideographs to unified ideographs first
    
    char_cache = set()
    
    prev_char = None
    for char in string:
        if (prev_char, char) not in char_cache:
            if prev_char and (is_cjk(prev_char) or prev_char in CENTERABLE_PUNCTATION) and ((0xfe00 <= ord(char) <= 0xfe0f) or (0xe0100 <= ord(char) <= 0xe01ef)):
                string = string.replace(f'{prev_char}{char}', prev_char)
            
        prev_char = char
        char_cache.add((prev_char, char))
        
        if char not in char_cache:
            if (0xf900 <= ord(char) <= 0xfaff) or (0x2f800 <= ord(char) <= 0x2fa1f):
                if char in COMPATIBILITY_CORRECTED_MAPPING:
                    value = COMPATIBILITY_CORRECTED_MAPPING[char]
                else:
                    value = unicodedata.normalize('NFKC', char)
                
                string = string.replace(char, value)
        
        char_cache.add(char)
        
    # start conversion
    
    char_cache = set()
    returned = string
    
    for char in string:
        if char not in char_cache:
            # initial conversion
            
            converted_value = char
            attr = ''
            
            dont_replace = False
            
            if char in VARIANTS_TABLE:
                converted_value, attr = VARIANTS_TABLE[char]
                
                if NOT_UNIFIABLE in attr:
                    dont_replace = not convert_not_unifiable
            
            # compatibility variants and IVS conversion
            
            value_base = converted_value
            attr_base = attr
            converted_ivs = None
            
            for compatibility_table in compatibility_tables_ordered:
                if value_base in compatibility_table:
                    value, attr = compatibility_table[value_base]
                    
                    if (ivs and (IVS_COMP_CLASH in attr)):
                        attr = attr_base
                        continue
                    else:
                        converted_value = value
                        break
            else:
                for ivs_table in ivs_tables_ordered:
                    if value_base in ivs_table:
                        converted_ivs, attr = ivs_table[value_base]
                        break
            
            # finalization
            
            char_cache.update({char, converted_value})
            
            for option, variant_set in [(alternate, ALTERNATE), (etymological, ETYMOLOGICAL), (tiao_na, TIAO_NA)]:
                if dont_replace:
                    break
                elif option:
                    dont_replace = variant_set in attr and REVERSE in attr
                else:
                    dont_replace = variant_set in attr and REVERSE not in attr
                        
            if not dont_replace and ord(char) <= 0xffff and ord(converted_value) > 0xffff:
                if supp_planes == CORE:
                    dont_replace = not (converted_value in SUPP_CORE_LIST)
                else:
                    dont_replace = not bool(supp_planes)
            
            if not dont_replace and converted_ivs:
                converted_value = converted_ivs
            
            # centralize punctation symbols
            
            if punctation_align_center and char in CENTERABLE_PUNCTATION:
                converted_value = f'{char}\ufe01'
                replace = True
            
            if char != converted_value and not dont_replace:
                returned = returned.replace(char, converted_value)
    
    return returned