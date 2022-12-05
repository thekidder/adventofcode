from collections import defaultdict, Counter

import functools
import math
import re
import sys

from helpers import *

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def build_range(r):
    [min,max] = r.split('-')
    return set(range(int(min),int(max)+1))


def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            [r1, r2] = line.strip().split(',')

            lines.append([build_range(r1), build_range(r2)])

    return lines

    # group by newlines
    # return grouped_input(filename, int)



def part1(filename):
    print(filename)
    input = parse_file(filename)
    ans = 0
    for s1,s2 in input:
        if s1.issubset(s2) or s2.issubset(s1):
            ans += 1
    print(f'ANSWER: {ans}')


def part2(filename):
    print(filename)
    input = parse_file(filename)
    ans = 0
    for s1,s2 in input:
        if not s1.isdisjoint(s2):
            ans += 1
    print(f'ANSWER: {ans}')


part2('example.txt')
part2('input.txt')
