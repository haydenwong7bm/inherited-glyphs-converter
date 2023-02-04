from collections import defaultdict
import re

__all__ = ['convert', 'CORE', 'ALL', 'J', 'K', 'T']

CORE = 'c'
ALL = '*'

J = 'j'
K = 'k'
T = 't'

INHERITED = 'i'

def _remove_jkt(attr):
    return re.sub('[jkt]', '', attr)

def _check_supp(a, b):
    return ord(a) <= 0xffff and ord(b) > 0xffff

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

with open('conversion-tables/radicals.txt', 'rt', encoding='utf-8') as file:
    RADICALS_VARIANTS_TABLE = {}
    
    for line in file:
        key_value = line.rstrip('\n').split('\t')
        key = key_value[0]
        value = key_value[1]
        
        RADICALS_VARIANTS_TABLE[key] = value

with open('conversion-tables/ivd-adobe-japan1.txt', 'rt', encoding='utf-8') as file:
    IVS_TABLE = {}
    
    for line in file:
        key_value = line.rstrip('\n').split('\t')
        key = key_value[0]
        value = key_value[1]
        
        IVS_TABLE[key] = value

def convert(string: str, *, use_supp_planes='c', use_compatibility='jkt', convert_inherited=True, use_ivs=False) -> str:
    if (not use_supp_planes) or (use_supp_planes not in {CORE, ALL}):
        raise TypeError
    
    if not use_supp_planes:
        use_supp_planes = ''
    
    compatibility_map = lambda x: {J: J_TABLE, K: K_TABLE, T: T_TABLE}[x]
    
    compatibility_order = [compatibility_map(i) for i in use_compatibility]
    
    returned = string
    
    for char in string:
        value = char
        replace = False
        
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
            returned = returned.replace(char, value)
            continue
        
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
            if use_ivs and value in IVS_TABLE:
                value = IVS_TABLE[value]
                replace = True
        
        if replace:
            returned = returned.replace(char, value)
    
    return returned