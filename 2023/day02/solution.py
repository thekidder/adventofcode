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
    games = []
    with open(filename, 'r') as f:
        for l in f:
            game = []
            (_, cubes) = l.split(':')
            sets = cubes.split(';')
            for s in sets:
                ss = []
                batches = s.split(',')
                for b in batches:
                    (num, color) = b.strip().split(' ')
                    bb = (int(num), color.strip())
                    ss.append(bb)
                game.append(ss)
            games.append(game)

        return games


def part1(filename):
    games = parse_file(filename)
    ans = 0
    for (i, game) in enumerate(games):
        if possible(game):
            ans += i + 1
    print(f'P1 {filename}: {ans}')


cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def possible(game):
    for s in game:
        for c in s:
            if cubes[c[1]] < c[0]:
                return False 
    return True


def power(game):
    least = defaultdict(int)
    for s in game:
        for c in s:
            least[c[1]] = max(least[c[1]], c[0])
    return functools.reduce(operator.mul, least.values(), 1)


def part2(filename):
    games = parse_file(filename)
    ans = functools.reduce(operator.add, map(power, games))
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
