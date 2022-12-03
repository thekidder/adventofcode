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

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            a = line[:len(line)//2]
            b = line[len(line)//2:]
            lines.append([a,b])

    return lines

    # group by newlines
    # return grouped_input(filename, int)



def parse_file2(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    return lines

def priority(item):
    if item <= 'Z':
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1

def part1(filename):
    print(filename)
    input = parse_file(filename)
    ans = 0
    for c in input:
        [a, b] = c
        a_set = set(a)
        b_set = set(b)
        for item in a_set:
            if item in b_set:
                ans += priority(item)
    print(f'ANSWER: {ans}')


def part2(filename):
    print(filename)
    input = parse_file2(filename)
    ans = 0
    while len(input) > 0:
        group = input[:3]
        a_set = set(group[0])
        b_set = set(group[1])
        c_set = set(group[2])

        for item in a_set:
            if item in b_set and item in c_set:
                ans += priority(item)
                break


        input = input[3:]
    print(f'ANSWER: {ans}')


part2('example.txt')
part2('input.txt')
