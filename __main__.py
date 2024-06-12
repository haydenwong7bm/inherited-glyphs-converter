import argparse
import importlib.util
import os.path as path

from inheritedglyphs import *

chardet_installed = importlib.util.find_spec("chardet") is not None

if chardet_installed:
    from chardet.universaldetector import UniversalDetector
    detector = UniversalDetector()

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='*')
parser.add_argument('-c', '--compatibility', default='jkt')
parser.add_argument('-s', '--supp', default='c')
parser.add_argument('-n', '--convert_not_unifiable', action='store_false')
parser.add_argument('-v', '--alternate', action='store_true')
parser.add_argument('-a', '--etymological', action='store_true')
parser.add_argument('-i', '--ivs', nargs='+')
parser.add_argument('-t', '--tiao_na', action='store_true')
parser.add_argument('-p', '--punctation', action='store_true')

args = parser.parse_args()

if args.compatibility == '_':
    args.compatibility = False

if args.supp == '_':
    args.supp = False

if not args.file:
    raise ValueError('file is missing')

for file in args.file:
    filename, file_ext = path.splitext(file)
    
    if chardet_installed:
        with open(file, 'rb') as input_file:
            detector.reset()
            for line in input_file:
                detector.feed(line)
                if detector.done:
                    break
        
        encoding = detector.result['encoding']
    else:
        encoding = 'utf-8'
    
    with (open(file, 'rt', encoding=encoding) as input_file,
          open(f'{filename}-converted{file_ext}', 'wt', encoding='utf-8') as output_file):
        contents = input_file.read()
        
        converted = convert(contents, \
        supp_planes=args.supp, \
        compatibility=args.compatibility, \
        convert_not_unifiable=args.convert_not_unifiable, \
        alternate=args.alternate, \
        etymological=args.etymological, \
        ivs=args.ivs, \
        tiao_na=args.tiao_na, \
        punctation_align_center=args.punctation)
        
        output_file.write(converted)