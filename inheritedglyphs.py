from collections import defaultdict
import re

__all__ = ['convert', 'CORE', 'ALL', 'J', 'K', 'T']

def _map(string: str, map_dict: dict={}) -> str:
    for key, value in map_dict.items():
        string = string.replace(key, value)
        
    return string

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

def convert(string: str, *, use_supp_planes='c', use_compatibility='jkt', convert_inherited=True) -> str:
    if use_supp_planes not in {False, 'c', '*'}:
        raise TypeError(f"must be either False, 'c' or '*', not {type(use_supp_planes)}")
    
    use_compatibility = ''.join(use_compatibility)
    regex = f'[{use_compatibility}{"i" * convert_inherited}]'
    
    for key, value in VARIANTS_TABLE.items():
        value, attr = value
        
        if not attr:
            string = string.replace(key, value)
        elif re.search(regex, attr):
            if re.search('[c*]', attr):
                if use_supp_planes in attr:
                    string = string.replace(key, value)
            else:
                string = string.replace(key, value)
        elif re.search('[c*]', attr):
            if use_supp_planes in attr:
                string = string.replace(key, value)
    
    for key, value in RADICALS_VARIANTS_TABLE.items():
        string = string.replace(key, value)
    
    return string