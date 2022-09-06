__all__ = ['convert']

def _file_to_dict(file):
    conversion_dict = {}
    
    for line in file:
        key_value = line.rstrip('\n').split('\t')
        key = key_value[0]
        value = key_value[1]
        
        conversion_dict[key] = value
        
    return conversion_dict

UNIFIABLE_VARIANTS = _file_to_dict(open('conversion-tables/unifiable_variants.txt', 'rt', encoding='utf-8'))
UNIFIABLE_VARIANTS_SUPP_CORE = _file_to_dict(open('conversion-tables/unifiable_variants_supp_core.txt', 'rt', encoding='utf-8'))
UNIFIABLE_VARIANTS_SUPP = _file_to_dict(open('conversion-tables/unifiable_variants_supp_planes.txt', 'rt', encoding='utf-8'))
J_COMPATIBILITY_VARIANTS = _file_to_dict(open('conversion-tables/j-compatibility_variants.txt', 'rt', encoding='utf-8'))
K_COMPATIBILITY_VARIANTS = _file_to_dict(open('conversion-tables/k-compatibility_variants.txt', 'rt', encoding='utf-8'))
INHERITED_VARIANTS = _file_to_dict(open('conversion-tables/inherited_variants.txt', 'rt', encoding='utf-8'))
INHERITED_VARIANTS_SUPP = _file_to_dict(open('conversion-tables/inherited_variants_supp_planes.txt', 'rt', encoding='utf-8'))
RADICALS_VARIANTS = _file_to_dict(open('conversion-tables/radicals.txt', 'rt', encoding='utf-8'))

def convert(string: str, *, use_supp_core=True, use_supp_planes=False, use_j=False, use_k=False, convert_variants=True) -> str:
    if use_supp_planes:
        use_supp_core = True
    
    for key, value in UNIFIABLE_VARIANTS.items():
        string = string.replace(key, value)
    
    for key, value in RADICALS_VARIANTS.items():
        string = string.replace(key, value)
    
    if use_supp_core:
        for key, value in UNIFIABLE_VARIANTS_SUPP_CORE.items():
            string = string.replace(key, value)
    
    if use_supp_planes:
        for key, value in UNIFIABLE_VARIANTS_SUPP.items():
            string = string.replace(key, value)
    
    if use_j:
        for key, value in J_COMPATIBILITY_VARIANTS.items():
            string = string.replace(key, value)
    
    if convert_variants:
        for key, value in INHERITED_VARIANTS.items():
            string = string.replace(key, value)
    
        if use_supp_planes:
            for key, value in INHERITED_VARIANTS_SUPP.items():
                string = string.replace(key, value)
    
    if use_k:
        for key, value in K_COMPATIBILITY_VARIANTS.items():
            string = string.replace(key, value)
    
    return string