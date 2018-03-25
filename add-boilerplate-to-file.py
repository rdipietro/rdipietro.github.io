#!/usr/bin/env python3

import argparse


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('file', type=str, help='The HTML file to modify')
parser.add_argument('boilerplate_file', type=str, help='The file with boilerplate')
args = parser.parse_args()

with open(args.boilerplate_file, 'r') as f:
    boilerplate = f.read()
    
with open(args.file, 'r') as f:
    contents = f.read()
    
if contents.count(boilerplate) > 0:
    print('{} has already been modified.'.format(args.file))
else:
    ind_at_blank = contents.find('\n\n') + 1
    contents = contents[:ind_at_blank] + boilerplate + contents[ind_at_blank:]
    with open(args.file, 'w') as f:
        f.write(contents)
    print('{} modified.'.format(args.file))
