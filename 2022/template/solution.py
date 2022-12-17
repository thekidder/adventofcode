from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.read()
        sections = lines.split('\n\n')

        return r
    # lines = []
    # with open(filename, 'r') as f:
    #     for line in f:
    #         lines.append(int(line))

    # return lines


def part1(filename):
    input = parse_file(filename)
    print(input)
    ans = 0
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    ans = 0
    print(f'P2 {filename}: {ans}')


part1('example.txt')
# part1('input.txt')

# part2('example.txt')
# part2('input.txt')
