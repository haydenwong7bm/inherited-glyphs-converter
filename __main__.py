import argparse
import os.path as path

from inheritedglyphs import *

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='*')
parser.add_argument('-c', '--compat', default='jkt')
parser.add_argument('-s', '--supp', default='c')
parser.add_argument('-n', '--not_unifiable', action='store_false')
parser.add_argument('-v', '--alternate', action='store_true')
parser.add_argument('-a', '--academic_correct', action='store_true')
parser.add_argument('-i', '--ivs', nargs='+')
parser.add_argument('-p', '--punctation', action='store_true')

args = parser.parse_args()

if args.compat == '_':
    args.compat = False

if args.supp == '_':
    args.supp = False

if not args.file:
    raise ValueError('file is missing')

for file in args.file:
    filename, file_ext = path.splitext(file)
    with (open(file, 'rt') as input_file,
        open(f'{filename}-converted{file_ext}', 'wt') as output_file):
        contents = input_file.read()
        converted = convert(contents, supp_planes=args.supp, compatibility=args.compat, convert_not_unifiable=args.not_unifiable, alternate=args.alternate, academic_correct=args.academic_correct, ivs=args.ivs, punctation_align_center=args.punctation)
        output_file.write(converted)