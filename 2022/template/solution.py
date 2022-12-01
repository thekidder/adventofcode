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
            lines.append(int(line))

    return lines

    # group by newlines
    # return grouped_input(filename, int)



def part1(filename):
    input = parse_file(filename)
    ans = 0
    print(f'ANSWER: {ans}')


def part2(filename):
    pass


part1('example.txt')
# part1('input.txt')
