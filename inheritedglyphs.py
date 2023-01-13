from collections import defaultdict
import re

__all__ = ['convert', 'CORE', 'ALL', 'J', 'K', 'T']

CORE = 'c'
ALL = '*'
J = 'j'
K = 'k'
T = 't'
INHERITED = 'i'

with open('conversion-tables/variants_list.txt', 'rt', encoding='utf-8') as file:
    VARIANTS_TABLE = dict()
    
    for line in file:
        key_value = line.rstrip('\n').split('\t')
        key = key_value[0]
        value = key_value[1]
        
        if len(key_value) >= 3:
            attr = key_value[2]
        else:
            attr = ''
        
        VARIANTS_TABLE[key] = (value, attr)

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
    if use_supp_planes not in {False, '', 'c', '*'}:
        raise TypeError
    
    if not use_supp_planes:
        use_supp_planes = ''
    
    def sort_order(x):
        if x == '' or 'i' in x:
            order = 0
        else:
            order = 2
            for option in use_compatibility:
                if option in x:
                    break
                else:
                    order += 2
            else:
                order = 0
        
        order += bool(re.search('[c*]', x))
        
        return order
    
    sorted_table = list(VARIANTS_TABLE.items())
    sorted_table.sort(key=lambda x: sort_order(x[1][1]))
    sorted_table = dict(sorted_table)
    
    use_compatibility = f'[{"".join(use_compatibility)}]'
    
    returned = string
    
    for char in string:
        if char in sorted_table:
            value, attr = sorted_table[char]
            
            replace = not ('*' in attr and use_supp_planes not in attr)
            
            if re.search('[jkt]', attr):
                replace = replace and re.search(use_compatibility, attr)
                
            else:
                replace = not ('*' in attr and use_supp_planes not in attr)
                
                if replace and ('i' in attr):
                    replace = convert_inherited
            
            if replace:
                returned = returned.replace(char, value)
        
        elif char in RADICALS_VARIANTS_TABLE:
            returned = returned.replace(char, RADICALS_VARIANTS_TABLE[char])
        
        if use_ivs and char in IVS_TABLE:
            returned = returned.replace(char, IVS_TABLE[char])
    
    return returned