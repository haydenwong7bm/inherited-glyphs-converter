from collections import defaultdict
import re
import unicodedata

__all__ = ['convert', 'CORE', 'ALL', 'J', 'K', 'T', 'NOT_UNIFIABLE', 'AD', 'MO']

CORE = 'c'
ALL = '*'

J = 'j'
K = 'k'
T = 't'

IVS_COMP_CLASH = "'"

ALTERNATE = 'v'

NOT_UNIFIABLE = 'n'

AD = 'ad'
MO = 'mo'
MS = 'ms'

def read_tsv(path):
    returned = {}
    
    with open(path, 'rt', encoding='utf-8') as file:
        for line in file:
            key_value = line.rstrip('\n').split('\t')
            
            key = key_value[0]
            value = key_value[1]
            
            returned[key] = value
    
    return returned

with open('conversion-tables/variants_list.txt', 'rt', encoding='utf-8') as file:
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
        
        remove_locale = lambda attr: re.sub('[jkt]', '', attr)
        
        no_attr = True
        
        if J in attr:
            J_TABLE[key] = value, remove_locale(attr)
            no_attr = False
        if K in attr:
            K_TABLE[key] = value, remove_locale(attr)
            no_attr = False
        if T in attr:
            T_TABLE[key] = value, remove_locale(attr)
            no_attr = False
        
        if no_attr:
            VARIANTS_TABLE[key] = value, attr
            
        if CORE in attr:
            SUPP_CORE_LIST.add(value)

COMPATIBILITY_CORRECTED_MAPPING = read_tsv('conversion-tables/compatibility_corrected_mapping.txt')

IVS_AD_TABLE = read_tsv('conversion-tables/ivs-adobe-japan1.txt')
IVS_MO_TABLE = None # read_tsv('conversion-tables/ivs-moji-joho.txt')
IVS_MS_TABLE = read_tsv('conversion-tables/ivs-mscs.txt')

def convert(string: str, *, supp_planes=CORE, compatibility=[J, K, T], convert_not_unifiable=True, alternate=False, ivs=False, punctation_align_center=False) -> str:
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
    
    for char in string:
        if char not in char_cache:
            if ivs and ((0xfe00 <= ord(char) <= 0xfe0f) or (0xe0100 <= ord(char) <= 0xe01ef)):
                string = string.replace(char, '')
            
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
            
            no_replace = False
            academic_variant = False
            alternate_variant = False
            
            if char in VARIANTS_TABLE:
                converted_value, attr = VARIANTS_TABLE[char]
                
                if NOT_UNIFIABLE in attr:
                    no_replace = not convert_not_unifiable
                
                if ALTERNATE in attr:
                    alternate_variant = True
            
            # compatibility variants/IVS conversion
            
            value_base = converted_value
            converted_ivs = ''
            
            for compatibility_table in compatibility_tables_ordered:
                if value_base in compatibility_table:
                    value, attr = compatibility_table[value_base]
                    
                    if (ivs and (K in compatibility) and (IVS_COMP_CLASH in attr)):
                        converted_value = value_base
                        continue
                    else:
                        if ALTERNATE in attr:
                            alternate_variant = True
                        
                        converted_value = value
                        
                        break
            else:
                for ivs_table in ivs_tables_ordered:
                    if value_base in ivs_table:
                        converted_ivs = ivs_table[value_base]
                        
                        break
            
            # finalization
            
            char_cache.add(char)
            char_cache.add(converted_value)
            
            if not alternate and alternate_variant:
                char, converted_value = converted_value, char
            
            if not no_replace and ord(char) <= 0xffff and ord(converted_value) > 0xffff:
                if supp_planes == CORE:
                    no_replace = not (converted_value in SUPP_CORE_LIST)
                else:
                    no_replace = not bool(supp_planes)
            
            if converted_ivs:
                converted_value = converted_ivs
            
            # centralize punctation symbols
            
            if punctation_align_center and char in '、。！，．：；？':
                converted_value = f'{char}\ufe01'
                replace = True
            
            if char != converted_value and not no_replace:
                returned = returned.replace(char, converted_value)
    
    return returned