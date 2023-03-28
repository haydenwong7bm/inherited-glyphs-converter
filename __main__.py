import argparse
import os.path as path
import sys

from inheritedglyphs import *

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='*')
parser.add_argument('-c', '--compat', default='jkt')
parser.add_argument('-s', '--supp', default='c')
parser.add_argument('-n', '--not_unifiable', action='store_true')
parser.add_argument('-i', '--ivs', nargs='*')

args = parser.parse_args()

if args.compat == '_':
    args.compat = False

if args.supp == '_':
    args.supp = False

for file in args.file:
    filename, file_ext = path.splitext(path.basename(file))
    with (open(file, 'rt') as input_file,
        open(f'{filename}-converted{file_ext}', 'wt') as output_file):
        contents = input_file.read()
        converted = convert(contents, use_supp_planes=args.supp, use_compatibility=args.compat, convert_not_unifiable=args.not_unifiable, use_ivs=args.ivs)
        output_file.write(converted)