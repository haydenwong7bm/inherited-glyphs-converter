from collections import defaultdict
import re

__all__ = ['convert', 'CORE', 'ALL', 'J', 'K', 'T', 'INHERITED', 'AJ1', 'MJ']

CORE = 'c'
ALL = '*'

J = 'j'
K = 'k'
T = 't'

INHERITED = 'i'

AJ1 = 'aj1'
MJ = 'mj'

def _remove_jkt(attr):
    return re.sub('[jkt]', '', attr)

def _check_supp(a, b):
    return ord(a) <= 0xffff and ord(b) > 0xffff

def _read_tsv(path):
    returned = {}
    
    with open(path, 'rt', encoding='utf-8') as file:
        for line in file:
            key_value = line.rstrip('\n').split('\t')
            key = key_value[0]
            value = key_value[1]
            
            returned[key] = value
    
    return returned

with open('conversion-tables/variants_list.txt', 'rt', encoding='utf-8') as file:
    VARIANTS_TABLE = dict()
    J_TABLE = dict()
    K_TABLE = dict()
    T_TABLE = dict()
    
    for line in file:
        key_value = line.rstrip('\n').split('\t')
        key = key_value[0]
        value = key_value[1]
        
        if len(key_value) >= 3:
            attr = key_value[2]
        else:
            attr = ''
        
        flag = True
        
        if J in attr:
            J_TABLE[key] = value, _remove_jkt(attr)
            flag = False
        if K in attr:
            K_TABLE[key] = value, _remove_jkt(attr)
            flag = False
        if T in attr:
            T_TABLE[key] = value, _remove_jkt(attr)
            flag = False
        
        if flag:
            VARIANTS_TABLE[key] = value, attr

RADICALS_VARIANTS_TABLE = _read_tsv('conversion-tables/radicals.txt')
IVS_AJ1_TABLE = _read_tsv('conversion-tables/ivs-adobe-japan1.txt')
IVS_MJ_TABLE = _read_tsv('conversion-tables/ivs-moji-joho.txt')

def convert(string: str, *, use_supp_planes='c', use_compatibility=[J, K, T], convert_inherited=True, use_ivs=False) -> str:
    if (not use_supp_planes) or (use_supp_planes not in {CORE, ALL}):
        raise TypeError
    if not use_supp_planes:
        use_supp_planes = ''
    
    if use_compatibility:
        compatibility_var_map = lambda x: {J: J_TABLE, K: K_TABLE, T: T_TABLE}[x]
        compatibility_order = [compatibility_var_map(i) for i in use_compatibility]
    else:
        compatibility_order = []
    
    if use_ivs:
        ivs_var_map = lambda x: {AJ1: AJ1_TABLE, MJ: MJ_TABLE}[x]
        if use_ivs:
            ivs_order = [ivs_var_map(i) for i in use_ivs]
    else:
        ivs_order = []
    
    returned = string
    for char in string:
        value = char
        replace = False
        
        # initial conversion
        
        if value in VARIANTS_TABLE:
            attr = VARIANTS_TABLE[value][1]
            
            if _check_supp(value, VARIANTS_TABLE[value][0]):
                replace = bool(use_supp_planes)
                if use_supp_planes == CORE:
                    replace = use_supp_planes in attr
            else:
                replace = True
            
            if replace and (INHERITED in attr):
                replace = convert_inherited
                
            if replace:
                value = VARIANTS_TABLE[value][0]
        elif char in RADICALS_VARIANTS_TABLE:
            value = RADICALS_VARIANTS_TABLE[value]
            replace = True
        
        # compatibility variants/IVS conversion
        
        for compatibility_table in compatibility_order:
            if value in compatibility_table:
                attr = compatibility_table[value][1]
                
                if _check_supp(value, compatibility_table[value][0]):
                    replace = bool(use_supp_planes)
                    if use_supp_planes == CORE:
                        replace = use_supp_planes in attr
                else:
                    replace = True
                
                if replace:
                    value = compatibility_table[value][0]
                    break
        else:
            for ivs_table in ivs_order:
                if value in ivs_table:
                    value = ivs_table[value]
                    replace = True
                    break
        
        if replace:
            returned = returned.replace(char, value)
    
    return returned