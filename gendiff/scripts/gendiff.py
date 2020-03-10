#!/usr/bin/env python3

import argparse
import json
from gendiff.scripts.gendiff_tool import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', metavar='FORMAT', help='set format of output')

    args = parser.parse_args()
    d1 = json.load(open(args.first_file))
    d2 = json.load(open(args.second_file))
    print(generate_diff(d1, d2))

if __name__ == '__main__':
    main()

