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
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            res, ops = line.split(':')
            ops = list(map(int, ops.split()))
            lines.append((int(res), ops))

    return lines




def computes(res, args):
    partials = set([args[0]])
    args = args[1:]
    while len(args) > 0:
        n = args[0]
        args = args[1:]
        next_partials = set()
        for p in partials:
            if p * n <= res:
                next_partials.add(p*n)
            ored = int(str(p) + str(n))
            if ored <= res:
                next_partials.add(ored)
            next_partials.add(p+n)
        partials = next_partials
    
    return res in partials


def part1(filename):
    input = parse_file(filename)
    ans = 0

    for res, args in input:
        # print(res, args)
        if computes(res, args):
            ans += res

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    ans = 0
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

# part2('example.txt')
# part2('input.txt')
