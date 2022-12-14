from collections import defaultdict, Counter

import itertools
import functools
import math
import re
import sys


def parse_pairs(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.read()
        sections = lines.split('\n\n')
        for s in sections:
            lines = s.split('\n')
            p1 = eval(lines[0])
            p2 = eval(lines[1])
            r.append((p1, p2))

    return r


def parse_all(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for l in lines:
            if len(l.strip()) == 0:
                continue
            r.append(eval(l))
    r.append([[2]])
    r.append([[6]])
    return r


def to_list(a):
    if type(a) == list:
        return a
    return [a]


def compare_element(item):
    l,r = item
    if l == r: return 0
    if l is None: return -1
    if r is None: return 1
    if type(l) == int and type(r) == int:
        return l - r
    return compare(to_list(l), to_list(r))


def compare(l, r):
    return next((x for x in map(compare_element, itertools.zip_longest(l, r)) if x), 0)


def part1(filename):
    input = parse_pairs(filename)
    ans = 0
    for i,(l,r) in enumerate(input):
        if compare(l,r) == -1:
            ans += (i + 1)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_all(filename)
    input = sorted(input, key=functools.cmp_to_key(compare))
    i = input.index([[2]])+1
    j = input.index([[6]])+1
    ans = i*j
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
part1('input.txt')

# part2('example.txt')
part2('input.txt')
