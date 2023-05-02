from collections import defaultdict
import re

__all__ = ['convert', 'CORE', 'ALL', 'J', 'K', 'T', 'NOT_UNIFIABLE', 'AJ1', 'MJ']

CORE = 'c'
ALL = '*'

J = 'j'
K = 'k'
T = 't'

ALTERNATE = 'v'

NOT_UNIFIABLE = 'n'

AJ1 = 'aj1'
MJ = 'mj'

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
IVS_AJ1_TABLE = read_tsv('conversion-tables/ivs-adobe-japan1.txt')
IVS_MJ_TABLE = read_tsv('conversion-tables/ivs-moji-joho.txt')

def convert(string: str, *, supp_planes='c', compatibility=[J, K, T], convert_not_unifiable=True, alternate=False, ivs=False, punctation_align_center=False) -> str:
    if not supp_planes:
        supp_planes = ''
    
    if supp_planes not in {'', CORE, ALL}:
        raise TypeError
    
    if compatibility:
        compatibility_var_map = lambda x: {J: J_TABLE, K: K_TABLE, T: T_TABLE}[x]
        compatibility_order = [compatibility_var_map(i) for i in compatibility]
    else:
        compatibility_order = []
    
    if ivs:
        ivs_var_map = lambda x: {AJ1: IVS_AJ1_TABLE, MJ: IVS_MJ_TABLE}[x]
        ivs_order = [ivs_var_map(i) for i in ivs]
    else:
        ivs_order = []
    
    # remove existing variation selectors
    
    for i in [*range(0xfe00, 0xfe0f+1), *range(0xe0100, 0xe01ef+1)]:
        string = string.replace(chr(i), '')
    
    # start conversion
    
    char_cache = set()
    
    returned = string
    for char in string:
        if char not in char_cache:
            value = char
            replace = False
            replace_alternate = False
            
            # initial conversion
            
            if char in VARIANTS_TABLE:
                value, attr = VARIANTS_TABLE[value]
                
                replace = True
                if replace and (NOT_UNIFIABLE in attr):
                    replace = convert_not_unifiable
                    
                if ALTERNATE in attr:
                    replace_alternate = True
            elif char in RADICALS_VARIANTS_TABLE:
                value = RADICALS_VARIANTS_TABLE[char]
                replace = True
            
            # compatibility variants/IVS conversion
            
            value_new = value
            for compatibility_table in compatibility_order:
                if value_new in compatibility_table:
                    value_new, attr = compatibility_table[value]
                    
                    if ALTERNATE in attr:
                        replace_alternate = True
                    
                    replace = True
                    break
            else:
                for ivs_table in ivs_order:
                    if value_new in ivs_table:
                        value_new = ivs_table[value]
                        
                        replace = True
                        break
            
            # centralize punctation
            
            if punctation_align_center and char in '、。！，．：；？':
                value = f'{char}\ufe01'
                replace = True
            
            char_cache.add(char)
            char_cache.add(value[0])
            
            if ord(char) <= 0xffff and ord(value_new[0]) > 0xffff:
                if bool(supp_planes):
                    value = value_new
            else:
                value = value_new
            
            if not alternate and replace_alternate:
                char, value = value, char
            
            if ord(char) <= 0xffff and ord(value) > 0xffff:
                replace = bool(supp_planes)
                if supp_planes == CORE:
                    replace = value in SUPP_CORE_LIST
            
            if replace:
                returned = returned.replace(char, value)
    
    return returned