from collections import defaultdict, Counter

import functools
import itertools
import heapq
import math
import re
import sys

from helpers import *

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def find(blocked, size):
    open = []
    start = (0, 0)
    end = (size, size)
    heapq.heappush(open, (0, start, 0))

    scores = defaultdict(lambda: math.inf)
    best_cost = math.inf

    while len(open):
        _, pos, cost = heapq.heappop(open)
        if pos == end and cost < best_cost:
            best_cost = cost
            break
        for dir in cardinals:
            n = vadd(pos, dir)
            if all(map(lambda x: x >= 0 and x <= size, n)) and n not in blocked:
                new_cost = cost + 1
                if new_cost < scores[n]:
                    scores[n] = new_cost
                    heapq.heappush(open, (mhn_dist(n, end)+new_cost, n, new_cost))
    return best_cost


def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            x,y = line.split(',')
            lines.append((int(x), int(y)))

    return lines


def part1(filename, size, bytes):
    input = parse_file(filename)
    ans = find(set(input[:bytes]), size)
    print(f'P1 {filename}: {ans}')


def part2(filename, size):
    input = parse_file(filename)
    ans = None
    for i in range(len(input)):
        print(i)
        cost = find(set(input[:i]), size)
        if cost == math.inf:
            ans = input[i-1]
            break

    print(f'P2 {filename}: {ans}, {i}')


# part1('example.txt', 6, 12)
# part1('input.txt', 70, 1024)

# part2('example.txt', 6)
# not 43, 12
part2('input.txt', 70)
