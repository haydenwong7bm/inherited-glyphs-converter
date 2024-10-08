import argparse
import importlib.util
import os.path as path

from inheritedglyphs import *

chardet_installed = importlib.util.find_spec("chardet") is not None

if chardet_installed:
    try:
        from chardet.universaldetector import UniversalDetector
        detector = UniversalDetector()
    except:
        chardet_installed = False

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='+')
parser.add_argument('-c', '--compatibility', default='jkt')
parser.add_argument('-s', '--supp', default='c')
parser.add_argument('-n', '--convert_not_unifiable', action='store_false')
parser.add_argument('-v', '--alternate', action='store_true')
parser.add_argument('-a', '--etymological', action='store_true')
parser.add_argument('-i', '--ivs', nargs='+')
parser.add_argument('-t', '--tiao_na', action='store_true')
parser.add_argument('-p', '--punctation', action='store_true')
parser.add_argument('-u', '--force_encoding', nargs='?', const='utf-8')

args = parser.parse_args()

if args.compatibility == '_':
    args.compatibility = False

if args.supp == '_':
    args.supp = False

for file in args.file:
    filename, file_ext = path.splitext(file)
    
    if chardet_installed and args.force_encoding is None:
        with open(file, 'rb') as input_file:
            detector.reset()
            for line in input_file:
                detector.feed(line)
                if detector.done:
                    break
        
        encoding = detector.result['encoding']
    else:
        encoding = 'utf-8' if args.force_encoding is None else args.force_encoding
    
    try:
        with open(file, 'rt', encoding=encoding) as input_file:
            contents = input_file.read()
    except UnicodeDecodeError:
        with open(file, 'rt', encoding='utf-8') as input_file:
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
    
    with open(f'{filename}-converted{file_ext}', 'wt', encoding='utf-8') as output_file:    
        output_file.write(converted)