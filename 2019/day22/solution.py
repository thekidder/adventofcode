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


def part1(data, pos=None, size=10):
    deck = list(range(size))
    input = parse(data)
    for ins in input:
        if ins.startswith('deal with increment'):
            new_deck = [0] * size
            incr = int(ins.split(' ')[-1])
            next_pos = 0
            for v in deck:
                new_deck[next_pos] = v
                next_pos = (next_pos + incr) % size
            deck = new_deck
        elif ins.startswith('cut'):
            amt = int(ins.split(' ')[-1])
            deck = deck[amt:] + deck[:amt]
        elif ins == 'deal into new stack':
            deck = list(reversed(deck))
        else:
            print(f'ERROR instruction {ins}')
    if pos is None:
        return deck
    for i, v in enumerate(deck):
        if v == pos:
            return i


def part2(data):
    input = parse(data)
    print(input)
    ans = 0
    return ans


check(part1, 'example1.txt', [0, 3, 6, 9, 2, 5, 8, 1, 4, 7], size=10)
check(part1, 'example2.txt', [3, 0, 7, 4, 1, 8, 5, 2, 9, 6], size=10)
check(part1, 'example3.txt', [6, 3, 0, 7, 4, 1, 8, 5, 2, 9], size=10)
check(part1, 'example4.txt', [9, 2, 5, 8, 1, 4, 7, 0, 3, 6], size=10)
check(part1, 'example4.txt', 3, size=10, pos=8)
exec(part1, 'input.txt', pos=2019, size=10007)

exec(part1, 'input.txt', pos=2020, size=119315717514047)

