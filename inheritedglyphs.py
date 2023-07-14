from collections import defaultdict
import re

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

RADICALS_VARIANTS_TABLE = read_tsv('conversion-tables/radicals.txt')
IVS_AD_TABLE = read_tsv('conversion-tables/ivs-adobe-japan1.txt')
IVS_MO_TABLE = None # read_tsv('conversion-tables/ivs-moji-joho.txt')
IVS_MS_TABLE = read_tsv('conversion-tables/ivs-mscs.txt')

def convert(string: str, *, supp_planes=CORE, compatibility=[J, K, T], convert_not_unifiable=True, alternate=False, ivs=False, punctation_align_center=False) -> str:
    if not supp_planes:
        supp_planes = ''
    
    if supp_planes not in {'', CORE, ALL}:
        raise TypeError
    
    if compatibility:
        compatibility_var_map = lambda x: {J: J_TABLE, K: K_TABLE, T: T_TABLE}[x]
        compatibility_tables_ordered = [compatibility_var_map(i) for i in compatibility]
    else:
        compatibility_tables_ordered = []
        compatibility = []
    
    if ivs:
        if 'mo' in ivs:
            raise NotImplementedError('Moji-Joho IVS conversion is temporarily removed due to inadequate conversion table')
        ivs_var_map = lambda x: {AD: IVS_AD_TABLE, MO: IVS_MO_TABLE, MS: IVS_MS_TABLE}[x]
        ivs_tables_ordered = [ivs_var_map(i) for i in ivs]
        
        # remove existing variation selectors
        for i in [*range(0xfe00, 0xfe0f+1), *range(0xe0100, 0xe01ef+1)]:
            string = string.replace(chr(i), '')
    else:
        ivs_tables_ordered = []
    
    # start conversion
    
    char_cache = set()
    returned = string
    
    for char in string:
        if char not in char_cache:
            converted_value = char
            
            replace = False
            replace_alternate = False
            
            # initial conversion
            
            if char in VARIANTS_TABLE:
                converted_value, attr = VARIANTS_TABLE[char]
                
                replace = True
                if replace and (NOT_UNIFIABLE in attr):
                    replace = convert_not_unifiable
                    
                if ALTERNATE in attr:
                    replace_alternate = True
            elif char in RADICALS_VARIANTS_TABLE:
                converted_value = RADICALS_VARIANTS_TABLE[char]
                
                replace = True
            
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
                            replace_alternate = True
                        
                        converted_value = value
                        
                        replace = True
                        break
            else:
                for ivs_table in ivs_tables_ordered:
                    if value_base in ivs_table:
                        converted_ivs = ivs_table[value_base]
                        
                        replace = True
                        break
            
            char_cache.add(char)
            char_cache.add(converted_value)
            
            if not alternate and replace_alternate:
                char, converted_value = converted_value, char
            
            if ord(char) <= 0xffff and ord(converted_value) > 0xffff:
                if supp_planes == CORE:
                    replace = value in SUPP_CORE_LIST
                else:
                    replace = bool(supp_planes)
            
            if converted_ivs:
                converted_value = converted_ivs
            
            # centralize punctation symbols
            if punctation_align_center and char in '、。！，．：；？':
                converted_value = f'{char}\ufe01'
                replace = True
            
            if replace:
                returned = returned.replace(char, converted_value)
    
    return returned