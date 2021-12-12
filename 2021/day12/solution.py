from collections import defaultdict, Counter

import re
import math
import sys

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    paths = []
    with open(filename, 'r') as f:
        for line in f:
            path = line.strip().split('-')
            paths.append((path[0],path[1]))

    exits = defaultdict(set)
    for path in paths:
        a,b = path
        exits[a].add(b)
        exits[b].add(a)

    return exits


def big(c):
    return c >= 'A' and c <= 'Z'


def make_paths(exits, path, next):
    if next in path and not big(next):
        return []

    if next == 'end':
        return [path[:] + [next]]

    paths = []
    path = path[:] + [next]
    for e in exits[next]:
        paths.extend(make_paths(exits, path, e))

    return paths

def part1(filename):
    input = parse_file(filename)
    ans = 0

    paths = []
    pos = 'start'
    for e in input[pos]:
        paths.extend(make_paths(input, [pos], e))

    print(f'ANSWER: {len(paths)}')


def can_add(cave, path):
    if cave == 'start':
        return False

    if big(cave):
        return True

    has_multiple_small_caves = any(map(lambda i: not big(i[0]) and i[1] > 1, path.items()))

    if path[cave] > 1:
        return False

    if has_multiple_small_caves:
        return path[cave] == 0
    
    return True


def make_paths2(exits, path, next):
    if next == 'end':
        return [path + Counter([next])]

    if not can_add(next, path):
        return []

    path = path + Counter([next])

    paths = []
    for e in exits[next]:
        paths.extend(make_paths2(exits, path, e))

    return paths


def part2(filename):
    input = parse_file(filename)

    paths = []
    pos = 'start'
    for e in input[pos]:
        paths.extend(make_paths2(input, Counter([pos]), e))
    
    print(f'ANSWER: {len(paths)}')


part2('input.txt')
