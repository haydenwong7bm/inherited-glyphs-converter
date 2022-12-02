from collections import defaultdict

__all__ = ['convert']

def _map(string: str, map_dict: dict={}) -> str:
    for key, value in map_dict.items():
        string = string.replace(key, value)
        
    return string

CORE = 'c'
SUPP = '*'
J = 'j'
K = 'k'
T = 't'
INHERITED = 'i'

with open('conversion-tables/variants_list.txt', 'rt', encoding='utf-8') as file:
    VARIANTS_LIST = defaultdict(dict)
    
    for line in file:
        key_value = line.rstrip('\n').split('\t')
        key = key_value[0]
        value = key_value[1]
        
        if len(key_value) == 3:
            target = key_value[2]
        else:
            target = ''
        
        VARIANTS_LIST[target][key] = value

with open('conversion-tables/radicals.txt', 'rt', encoding='utf-8') as file:
    RADICALS_VARIANTS = {}
    
    for line in file:
        key_value = line.rstrip('\n').split('\t')
        key = key_value[0]
        value = key_value[1]
        
        RADICALS_VARIANTS[key] = value

def convert(string: str, *, use_supp_core=True, use_supp_planes=False, use_j=False, use_k=False, use_t=False, convert_variants=True) -> str:
    if use_supp_planes:
        use_supp_core = True
    
    string = _map(string, VARIANTS_LIST[''])
    string = _map(string, RADICALS_VARIANTS)
    
    if use_supp_core:
        string = _map(string, VARIANTS_LIST[CORE])
    
    if use_supp_planes:
        string = _map(string, VARIANTS_LIST[SUPP])
    
    if convert_variants:
        string = _map(string, VARIANTS_LIST[INHERITED])
        
        if use_supp_core:
            string = _map(string, VARIANTS_LIST[INHERITED + CORE])
            
        if use_supp_planes:
            string = _map(string, VARIANTS_LIST[INHERITED + SUPP])
    
    if use_j:
        string = _map(string, VARIANTS_LIST[J])
    
    if use_t and use_supp_core:
        string = _map(string, VARIANTS_LIST[T + CORE])
    
    if use_k:
        string = _map(string, VARIANTS_LIST[K])
    
    if use_t and use_supp_planes:
        string = _map(string, VARIANTS_LIST[T])
        
    return string