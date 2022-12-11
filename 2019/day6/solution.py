from collections import defaultdict, Counter

import functools
import math
import re
import sys


# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip().split(')'))

    return lines


def norbits(orbits, body, stop = None):
    n = 0
    while body in orbits and body != stop:
        n += 1
        body = orbits[body]
    return n


def part1(filename):
    input = parse_file(filename)
    orbits = {}
    bodies = set()
    for body,satellite in input:
        orbits[satellite] = body
        bodies.add(body)
        bodies.add(satellite)
    ans = 0
    for b in bodies:
        ans += norbits(orbits,b)
    print(f'P1 {filename}: {ans}')


def transitive_orbits(orbits, body, satellite):
    while satellite in orbits    and satellite != body:
        satellite = orbits[satellite]
    return satellite == body


def part2(filename):
    input = parse_file(filename)
    orbits = {}
    bodies = set()
    for body,satellite in input:
        orbits[satellite] = body
        bodies.add(body)
        bodies.add(satellite)

    dest = orbits['SAN']
    s = None
    n = 0
    for b in bodies:
        if transitive_orbits(orbits, b, dest) and transitive_orbits(orbits, b, 'YOU') and norbits(orbits, b) > n:
            n = norbits(orbits, b)
            s  = b

    ans = norbits(orbits, 'YOU', s) + norbits(orbits, dest, s) - 1
    print(f'P2 {filename}: {ans}')
    

part1('example.txt')
part1('input.txt')

part2('example2.txt')
part2('input.txt')
