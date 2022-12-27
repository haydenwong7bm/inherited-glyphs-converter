import argparse
import os.path as path
import sys

from inheritedglyphs import *

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o', '--options', action='store_true')
parser.add_argument('-j', action='store_true')
parser.add_argument('-k', action='store_true')
parser.add_argument('-t', action='store_true')
parser.add_argument('-s', '--supp', default=False)
parser.add_argument('-i', '--inherited', action='store_true')
parser.add_argument('-I', '--ivs', action='store_true')

args = parser.parse_args()

if not args.options: # default options
    args.j = True
    args.k = True
    args.t = True
    args.supp = 'c'
    args.inherited = True
    args.ivs = False

compatibility_args = 'j' * args.j + 'k' * args.k + 't' * args.t

filename, file_ext = path.splitext(path.basename(args.file))
with open(args.file, 'rt') as input_file, open(f'{filename}-converted{file_ext}', 'wt') as output_file:
    contents = input_file.read()
    converted = convert(contents, use_supp_planes=args.supp, use_compatibility=compatibility_args, convert_inherited=args.inherited, use_ivs=args.ivs)
    output_file.write(converted)