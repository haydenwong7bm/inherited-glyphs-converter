import argparse
import os.path as path

from inheritedglyphs import *

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str)
parser.add_argument('-j', action='store_true')
parser.add_argument('-k', action='store_true')
parser.add_argument('-r', action='store_false')
parser.add_argument('-s', action='store_true')
parser.add_argument('-sc', action='store_false')
parser.add_argument('-tc', action='store_false')

args = parser.parse_args()

if args.s:
    args.sc = False

filename, file_ext = path.splitext(path.basename(args.file))
with open(args.file, 'rt') as file_read, open(f'{filename}-converted{file_ext}', 'wt') as file_write:
    file_write.write(convert(file_read.read(), use_supp_core=args.sc, use_supp_planes=args.s, use_j=args.j, use_k=args.k, use_t=args.t, convert_variants=args.r))