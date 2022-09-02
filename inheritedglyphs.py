__all__ = ['convert']

def _file_to_dict(file):
    conversion_dict = {}
    
    for line in file:
        key_value = line.rstrip('\n').split('\t')
        key = key_value[0]
        value = key_value[1]
        
        conversion_dict[key] = value
        
    return conversion_dict

CONVERSION_DICT_UNIFIABLE = _file_to_dict(open('conversion-tables/unifiable_variants.txt', 'rt', encoding='utf-8'))
CONVERSION_DICT_UNIFIABLE_SUPP = _file_to_dict(open('conversion-tables/unifiable_variants_supp_planes.txt', 'rt', encoding='utf-8'))
CONVERSION_DICT_J = _file_to_dict(open('conversion-tables/j-compatibility_variants.txt', 'rt', encoding='utf-8'))
CONVERSION_DICT_K = _file_to_dict(open('conversion-tables/k-compatibility_variants.txt', 'rt', encoding='utf-8'))
CONVERSION_DICT_INHERITED = _file_to_dict(open('conversion-tables/inherited_variants.txt', 'rt', encoding='utf-8'))
CONVERSION_DICT_INHERITED_SUPP = _file_to_dict(open('conversion-tables/inherited_variants_supp.txt', 'rt', encoding='utf-8'))

def convert(string: str, *, use_supp_planes=True, use_j=False, use_k=False, convert_variant=True) -> str:
    for key, value in CONVERSION_DICT_UNIFIABLE.items():
        string = string.replace(key, value)
    
    if use_supp_planes:
        for key, value in CONVERSION_DICT_UNIFIABLE_SUPP.items():
            string = string.replace(key, value)
    
    if use_j:
        for key, value in CONVERSION_DICT_J.items():
            string = string.replace(key, value)
        
    if convert_variant:
        for key, value in CONVERSION_DICT_INHERITED.items():
            string = string.replace(key, value)
            
        if use_supp_planes:
            for key, value in CONVERSION_DICT_INHERITED_SUPP.items():
                string = string.replace(key, value)
        
    if use_k:
        for key, value in CONVERSION_DICT_K.items():
            string = string.replace(key, value)
    
    return string