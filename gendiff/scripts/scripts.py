#!/usr/bin/env python3

from gendiff.generate_diff import gendiff_main
from gendiff.cli import take_arguments


def main():
    parser = take_arguments()
    args = parser.parse_args()
    print(gendiff_main(args.path_to_file1, args.path_to_file2, args.format))


if __name__ == '__main__':
    main()
