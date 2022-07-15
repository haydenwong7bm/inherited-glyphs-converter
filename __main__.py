import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('file', default=None)
parser.add_argument('-j', '--use_j', action='store_true')
parser.add_argument('-k', '--use_k', action='store_true')
args = parser.parse_args()

__all__ = ['convert']

def _file_to_dict(file):
    conversion_dict = {}
    
    for line in file:
        key_value = line.rsplit('\n').split('\t')
        key = key_value[0]
        value = key_value[1]
        
        conversion_dict[key] = value
        
    return conversion_dict

CONVERSION_DICT_SCS = _file_to_dict(open('conversion-tables/variants-scs.txt', 'rt', encoding='utf-8'))
CONVERSION_DICT_J = _file_to_dict(open('conversion-tables/variants-compatibility-j.txt', 'rt', encoding='utf-8'))
CONVERSION_DICT_K = _file_to_dict(open('conversion-tables/variants-compatibility-k.txt', 'rt', encoding='utf-8'))

def convert(string: str, use_j=False, use_k=False) -> str:
    for key, value in CONVERSION_DICT_SCS.items():
        string = string.replace(key, value)
        
    if use_j:
        for key, value in CONVERSION_DICT_J.items():
            string = string.replace(key, value)
        
    if use_k:
        for key, value in CONVERSION_DICT_K.items():
            string = string.replace(key, value)
            
    return string

if __name__ == '__main__':
    filename, file_ext = os.path.splitext(args.file)
    with open(args.file, 'rt') as file_read, open(f'{filename}-converted.{file_ext}', 'rt') as file_write:
        file_write.write(convert(file_read.read(), args.use_j, args.use_k))