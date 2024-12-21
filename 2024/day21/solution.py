from collections import defaultdict, Counter

import functools
import itertools
import math
import random
import re
import sys

from helpers import *

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        lines = []
        with open(filename, 'r') as f:
            for line in f:
                lines.append(line.strip())

        return lines


def generate_robot_fn(grid, cost, loc):
    for dir in cardinals:
        n = vadd(loc, dir)
        if n in grid and grid[n] != '.':
            cost = 1
            yield (cost + 1, n)


dirs = {
    (-1,  0): '<',
    ( 1,  0): '>',
    ( 0,  1): 'v',
    ( 0, -1): '^',
}


def path_to_dirs(path):
    for a,b in zip(path[:-1], path[1:]):
        if a == b:
            yield 'A'
        else:
            dir = vsub(b, a)
            yield dirs[dir]
    yield 'A'


# def filter_seq(seq):
#     dirs_since_a = set()
#     for i, c in enumerate(seq):
#         if c == 'A':
#             dirs_since_a = set()
#         else:
#             if i > 0 and c in dirs_since_a and seq[i-1] != c:
#                 # print('NO ', seq)
#                 return False
#             dirs_since_a.add(c)
#     # print('YES', seq)
#     return True


def filter_seqs(next_seqs, min_len):
    for seq in next_seqs:
        if len(seq) == min_len:# and filter_seq(seq):
            yield seq


def seq_len(code):
    keypad,kw,kh = parse_grid('keypad.txt')
    robot,rw,rh = parse_grid('robot.txt')
    nrobots = 2
    keypads = [keypad] + [robot] * nrobots

    seqs = set([code])
    for i,keypad in enumerate(keypads):
        print(f'{i}/{len(keypads)} depth')
        next_seqs = set()
        for code in seqs:
            next_seqs.update(get_seqs(code, keypad))
        l = math.inf
        for seq in next_seqs:
            l = min(l, len(seq))
        seqs = list(filter_seqs(next_seqs, l))
        seqs = random.sample(seqs, min(10, len(seqs)))
        print('example seq', seqs[0])

        # print(seqs)

    l = math.inf
    for seq in seqs:
        l = min(l, len(seq))
    return l


def gen_path(keypad, start, end, dirs):
    path = [start]
    pos = start
    for d in dirs:
        while mhn_dist(vadd(d, pos), end) < mhn_dist(pos, end):
            if keypad[vadd(d, pos)] == '.':
                return None
            path.append(vadd(d, pos))
            pos = path[-1]
    return path


def gen_paths(keypad, start, end):
    total_dist = mhn_dist(start, end)
    sorted_dirs = [d for d in dirs.keys() if mhn_dist(vadd(d, start), end) < total_dist]

    p1 = gen_path(keypad, start, end, sorted_dirs)
    p2 = None
    if len(sorted_dirs) > 1:
        p2 = gen_path(keypad, start, end, reversed(sorted_dirs))

    r = []
    if p1 is not None:
        r.append(p1)
    if p2 is not None:
        r.append(p2)
    return r
    


def get_seqs(code, keypad):
    pos_on_keypad = {}

    for k,v in keypad.items():
        pos_on_keypad[v] = k

    start_pos = pos_on_keypad['A']
    code_paths = [[]]

    for button in code:
        next_code_paths = []
        for path in code_paths:
            pos = path[-1] if len(path) else start_pos
            if pos != pos_on_keypad[button]:
                # print(pos, pos_on_keypad[button])
                # c,p = a_star(keypad, pos, pos_on_keypad[button], generate_robot_fn, est_grid_fn)
                p = gen_paths(keypad, pos, pos_on_keypad[button])
                for p in p:
                    next_code_paths.append(path + p)
            else:
                next_code_paths.append(path + [pos])
        code_paths = next_code_paths

    seqs = list(map(lambda x: ''.join(path_to_dirs(x)), code_paths))
    # seq = ''
    # for d in path_to_dirs(code_path):
    #     seq += d

    return seqs


def part1(filename):
    input = parse_file(filename)
    ans = 0

    for code in input:
        print(seq_len(code), int(code[:-1]))
        ans += seq_len(code) * int(code[:-1])

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    ans = 0



    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

# part2('example.txt')
# part2('input.txt')
