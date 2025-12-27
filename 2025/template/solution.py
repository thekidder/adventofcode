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


def parse(input):
    return input.split('\n')


def part1(data):
    input = parse(data)
    print(input)
    ans = 0
    return ans


def part2(data):
    input = parse(data)
    print(input)
    ans = 0
    return ans


check(part1, 'example.txt', 1)
exec(part1, 'input.txt')

# check(part2, 'example.txt', 1)
# exec(part2, 'input.txt')
