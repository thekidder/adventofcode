from collections import defaultdict, Counter

import itertools
import functools
import math
import re
import sys


def parse(s):
    return eval(s)

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.read()
        sections = lines.split('\n\n')
        for s in sections:
            lines = s.split('\n')
            p1 = parse(lines[0])
            p2 = parse(lines[1])
            r.append((p1, p2))

    return r

def compare(l, r):
    # print(f'CHECK {l} {r}')
    for l1, r1 in itertools.zip_longest(l, r):
        if l1 is None:
            return 1
        if r1 is None:
            return -1
        # print(f'LOOP {l1} {r1}')
        if type(l1) == int and type(r1) == int:
            if l1 == r1:
                # print(f'CONT {l1} {r1}')
                continue
            # print(f'{l1} {r1}')
            return 1 if l1 < r1 else -1
        elif type(l1) != int and type(r1) != int:
            c = compare(l1, r1)
            if c:
                return c
        elif type(l1) != int:
            c = compare(l1, [r1])
            if c:
                return c
        else:
            c = compare([l1], r1)
            if c:
                return c
    return 0

def part1(filename):
    input = parse_file(filename)
    print(input)
    ans = 0
    for i,(l,r) in enumerate(input):
        if compare(l,r) == 1:
            ans += (i +1)
            print(f'got index {i+1}')
            # ans += (i+1)
    print(f'P1 {filename}: {ans}')


def parse_all(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for l in lines:
            if len(l.strip()) == 0:
                continue
            r.append(parse(l))
    r.append([[2]])
    r.append([[6]])
    return r


def part2(filename):
    input = parse_all(filename)
    input = sorted(input, key=functools.cmp_to_key(compare), reverse=True)
    i = input.index([[2]])+1
    j = input.index([[6]])+1
    ans = i*j
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

part2('example.txt')
part2('input.txt')
