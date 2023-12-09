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
            lines.append(list(map(int, line.split())))

    return lines


def predict(history):
    stacks = [history]
    while not all(map(lambda x: x == 0, stacks[-1])):
        curr = stacks[-1]
        diffs = [x - y for x, y in zip(curr[1:], curr[:-1])]
        stacks.append(diffs)
    next = 0
    for stack in reversed(stacks):
        next = stack[-1] + next
    return next


def part1(filename):
    input = parse_file(filename)
    ans = sum(map(predict, input))
    print(f'P1 {filename}: {ans}')


def predict_back(history):
    stacks = [history]
    while not all(map(lambda x: x == 0, stacks[-1])):
        curr = stacks[-1]
        diffs = [x - y for x, y in zip(curr[1:], curr[:-1])]
        stacks.append(diffs)
    next = 0
    for stack in reversed(stacks):
        next = stack[0] - next

    # stack[0] - next = prev
    # next + prev = stack[0]
    # next = stack
    return next


def part2(filename):
    input = parse_file(filename)
    ans = sum(map(predict_back, input))
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
