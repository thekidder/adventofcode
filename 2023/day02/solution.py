from collections import defaultdict

import functools
import operator
import re

pattern = re.compile('(\d+) (\w+)')

def parse_file(filename):
    games = []
    with open(filename, 'r') as f:
        for l in f:
            colmax = defaultdict(int)
            for m in pattern.findall(l):
                colmax[m[1]] = max(int(m[0]), colmax[m[1]])
            games.append(colmax)

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
    for color,num in game.items():
        if num > cubes[color]:
            return False 
    return True


def power(game):
    least = defaultdict(int)
    for color,num in game.items():
        least[color] = max(least[color], num)
    return functools.reduce(operator.mul, least.values(), 1)


def part2(filename):
    games = parse_file(filename)
    ans = functools.reduce(operator.add, map(power, games))
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
