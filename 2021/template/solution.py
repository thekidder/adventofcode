from collections import defaultdict, Counter

import re
import math
import sys

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


def part1(filename):
    ans = 0
    print(f'ANSWER: {ans}')


def part2(filename):
    pass


part1('example.txt')
