__all__ = ['convert']

def _file_to_dict(file) -> dict:
    conversion_dict = {}
    
    for line in file:
        key_value = line.rstrip('\n').split('\t')
        key = key_value[0]
        value = key_value[1]
        
        conversion_dict[key] = value
        
    return conversion_dict

def _map(string: str, map_dict: dict={}) -> str:
    for key, value in map_dict.items():
        string = string.replace(key, value)
        
    return string

UNIFIABLE_VARIANTS = _file_to_dict(open('conversion-tables/unifiable_variants.txt', 'rt', encoding='utf-8'))
UNIFIABLE_VARIANTS_SUPP_CORE = _file_to_dict(open('conversion-tables/unifiable_variants_supp_core.txt', 'rt', encoding='utf-8'))
UNIFIABLE_VARIANTS_SUPP = _file_to_dict(open('conversion-tables/unifiable_variants_supp_planes.txt', 'rt', encoding='utf-8'))

J_COMPATIBILITY_VARIANTS = _file_to_dict(open('conversion-tables/j-compatibility_variants.txt', 'rt', encoding='utf-8'))
K_COMPATIBILITY_VARIANTS = _file_to_dict(open('conversion-tables/k-compatibility_variants.txt', 'rt', encoding='utf-8'))
T_COMPATIBILITY_VARIANTS_CORE = _file_to_dict(open('conversion-tables/t-compatibility_variants_core.txt', 'rt', encoding='utf-8'))

INHERITED_VARIANTS = _file_to_dict(open('conversion-tables/inherited_variants.txt', 'rt', encoding='utf-8'))
INHERITED_VARIANTS_SUPP = _file_to_dict(open('conversion-tables/inherited_variants_supp_planes.txt', 'rt', encoding='utf-8'))

RADICALS_VARIANTS = _file_to_dict(open('conversion-tables/radicals.txt', 'rt', encoding='utf-8'))

def convert(string: str, *, use_supp_core=True, use_supp_planes=False, use_j=False, use_k=False, use_t=False, convert_variants=True) -> str:
    if use_supp_planes:
        use_supp_core = True
    
    string = _map(string, UNIFIABLE_VARIANTS)
    string = _map(string, RADICALS_VARIANTS)
    
    if use_supp_core:
        string = _map(string, UNIFIABLE_VARIANTS_SUPP_CORE)
    
    if use_supp_planes:
        string = _map(string, UNIFIABLE_VARIANTS_SUPP)
    
    if convert_variants:
        string = _map(string, INHERITED_VARIANTS)
    
    if use_j:
        string = _map(string, J_COMPATIBILITY_VARIANTS)
    
    if use_t and use_supp_core:
        string = _map(string, T_COMPATIBILITY_VARIANTS_CORE)
    
    if use_k:
        string = _map(string, K_COMPATIBILITY_VARIANTS)
    
    '''
    if use_t and use_supp_planes:
        string = _map(string, T_COMPATIBILITY_VARIANTS)
    '''
    
    return string