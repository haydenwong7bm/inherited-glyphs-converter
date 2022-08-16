import argparse
import os

from inheritedglyphs import *

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str)
parser.add_argument('-j', '--use_j', action='store_true')
parser.add_argument('-k', '--use_k', action='store_true')
parser.add_argument('-r', '--use_inherited', action='store_false')
parser.add_argument('-s', '--use_supp_planes', action='store_false')

args = parser.parse_args()

filename, file_ext = os.path.splitext(args.file)
with open(args.file, 'rt') as file_read, open(f'{filename}-converted{file_ext}', 'wt') as file_write:
    file_write.write(convert(file_read.read(), use_supp_planes=args.use_supp_planes, use_j=args.use_j, use_k=args.use_k, use_inherited=args.use_inherited))