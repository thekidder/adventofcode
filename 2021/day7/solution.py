from collections import defaultdict, Counter

import re
import math
import sys

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    with open(filename, 'r') as f:
        pos = [int(n) for n in f.readline().split(',')]
        return pos


def part1(filename):
    crabs = parse_file(filename)
    min = 100000000
    min_pos = 0
    for p in crabs:
        cost = 0
        for c in crabs:
            cost += abs(c - p)
        if cost < min:
            min = cost
            min_pos = p
    print(f'ANSWER: {min} {min_pos}')


def calccost(delta):
    i = 0
    for n in range(1, delta+1):
        i += n
    return i

def part2(filename):
    crabs = parse_file(filename)
    min = 100000000
    min_pos = 0
    for p in range(max(crabs)):
        cost = 0
        for c in crabs:
            steps = abs(c - p)
            cost += calccost(steps)
        if cost < min:
            min = cost
            min_pos = p
    print(f'ANSWER: {min} {min_pos}')


print(calccost(0))
part2('input.txt')
