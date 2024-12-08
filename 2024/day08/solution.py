import itertools

from helpers import *


def all_signal_pairs(input):
    signals = set([v for v in input.values() if v != '.'])

    for signal in signals:
        locs = [p for p,v in input.items() if v == signal]
        for a,b in itertools.combinations(locs, 2):
            yield a,b


def part1(filename):
    input,_,_ = parse_grid(filename)
    antinodes = set()

    for a,b in all_signal_pairs(input):
        diff = vsub(a,b)
        a = vadd(a, diff)
        if a in input:
            antinodes.add(a)
        b = vsub(b, diff)
        if b in input:
            antinodes.add(b)

    ans = len(antinodes)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input,_,_ = parse_grid(filename)
    antinodes = set()

    for a,b in all_signal_pairs(input):
        diff = vsub(a,b)
        while a in input:
            antinodes.add(a)
            a = vadd(a, diff)
        while b in input:
            antinodes.add(b)
            b = vsub(b, diff)
    ans = len(antinodes)
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
