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
    with open(filename, 'r') as f:
        return list(map(int, f.read()))


def vals_of(i, x):
    return len(list(filter(lambda e: e == x, i)))

def part1(filename, w, h):
    input = parse_file(filename)
    layers = [input[l*w*h:(l+1)*w*h] for l in range(len(input)//(w*h))]
    layers.sort(key=lambda x: vals_of(x, 0))
    ans = vals_of(layers[0], 1) * vals_of(layers[0], 2)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    ans = 0
    print(f'P2 {filename}: {ans}')


part1('example.txt', 3, 2)
part1('input.txt', 25,6)

# part2('example.txt')
# part2('input.txt')
