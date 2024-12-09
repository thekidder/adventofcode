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
    r = []
    id = 0
    with open(filename, 'r') as f:
        lines = f.read()
        for i,c in enumerate(map(int, lines)):
            if i % 2 == 0:
                for _ in range(c):
                    r.append(id)
                id += 1
            else:
                for _ in range(c):
                    r.append(None)
    return r


def parse_file2(filename):
    r = []
    id = 0
    pos = 0
    with open(filename, 'r') as f:
        lines = f.read()
        for i,c in enumerate(map(int, lines)):
            if i % 2 == 0:
                r.append((pos, id, c))
                id += 1
                pos += c
            else:
                pos += c
    return r


def last(li):
    for i in reversed(range(len(li))):
        if li[i] is not None:
            return i


def part1(filename):
    input = parse_file(filename)
    # print(input)

    while True:
        try:
            gap = input.index(None)
            m = last(input)

            if gap >= m:
                break

 
            input[gap] = input[m]
            input[m] = None
        except:
            break

    ans = 0#unctools.reduce(lambda acc, x: acc + x[0]*x[1], enumerate(input))
    for i,x in enumerate(input):
        if x is not None:
            ans += i*x

    print(f'P1 {filename}: {ans}')


def position_of(input, id):
    for i in range(len(input)-1, 0, -1):
        if input[i][1] == id:
            return i
    print('ERR')
    return None

def part2(filename):
    input = parse_file2(filename)
    # print(input)
    # sys.exit(0)
    # positions = {}
    # for i, x in enumerate(input):
    #     positions[x[1]] = i
    # positions = dict(map(lambda x: (x[1], x[0]), input))
    id = input[-1][1]

    while id > 0:
        ind = position_of(input, id)
        # print(input,id,ind)
        pos,id,ln = input[ind]

        for i in range(ind):
            gap_size = input[i+1][0]  - (input[i][0] + input[i][2])
            if gap_size >= ln:
                # print(f'found gap of {gap_size} at {i} for {id}')
                del input[ind]
                input.insert(i+1, (input[i][0] + input[i][2], id, ln))
                break

        id -= 1


    # print(input)

    ans = 0
    for pos,id,ln in input:
        for offset in range(ln):
            ans += (pos + offset) * id

    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

part2('example.txt')
# not 6304576712958
part2('input.txt') 
