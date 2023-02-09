import argparse
import os.path as path
import sys

from inheritedglyphs import *

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='*')
parser.add_argument('-o', '--options', action='store_true')
parser.add_argument('-c', '--comp', default=False)
parser.add_argument('-s', '--supp', default=False)
parser.add_argument('-i', '--inherited', action='store_true')
parser.add_argument('-I', '--ivs', nargs='*')

args = parser.parse_args()

if not args.options: # default options
    args.comp = 'jkt'
    args.supp = 'c'
    args.inherited = True
    args.ivs = False

for file in args.file:
    filename, file_ext = path.splitext(path.basename(file))
    with (open(file, 'rt') as input_file,
        open(f'{filename}-converted{file_ext}', 'wt') as output_file):
        contents = input_file.read()
        converted = convert(contents, use_supp_planes=args.supp, use_compatibility=args.comp, convert_inherited=args.inherited, use_ivs=args.ivs)
        output_file.write(converted)