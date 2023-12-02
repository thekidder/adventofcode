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
    # lines = []
    # with open(filename, 'r') as f:
    #     for line in f:
    #         lines.append(int(line))

    # return lines


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
    l = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for s in game:
        for c in s:
            if c[0] > l[c[1]]:
                l[c[1]] = c[0]
    return l['red']*l['blue']*l['green']


def part2(filename):
    games = parse_file(filename)
    ans = 0
    for (i, game) in enumerate(games):
        ans += power(game)
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

part2('example.txt')
part2('input.txt')
