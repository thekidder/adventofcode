from collections import defaultdict, Counter

import functools
import itertools
import math
import random
import sys

from helpers import *

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


# costs = {
#     '<': 60773707514,
#     '>':  42672313154,
#     '^':  43706025078,
#     'v':  53421889593,
#     'A':  1,
# }

dirs = {
    (-1,  0): '<',
    ( 0,  1): 'v',
    ( 0, -1): '^',
    ( 1,  0): '>',
}


def path_to_dirs(path):
    for a,b in zip(path[:-1], path[1:]):
        if a == b:
            yield 'A'
        else:
            dir = vsub(b, a)
            yield dirs[dir]
    yield 'A'


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
        # print('example seq', seqs[0])

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

robot_keypad = None
robot_pos = None


costs = {
    '<': 34239478182,
    'v':  31694263025,
    '^':  25192224696,
    '>':  24175432924,
    'A':  1,
}

@functools.cache
def seq_to_seq(code):
    global seq_len_cache
    options = seq_to_seqs(code)

    best = None
    best_cost = math.inf

    for op in options:
        cost = functools.reduce(lambda acc, x: acc + costs[x], op, 0)
        if cost < best_cost:
            best_cost = cost
            best = op
    # print(code, best, best_cost)
    return best


def seq_to_seqs(code):
    global robot_keypad, robot_pos
    start_pos = robot_pos['A']
    code_paths = [[]]

    for button in code:
        next_code_paths = []
        for path in code_paths:
            pos = path[-1] if len(path) else start_pos
            if pos != robot_pos[button]:
                # print(pos, pos_on_keypad[button])
                # c,p = a_star(robot_keypad, pos, robot_pos[button], generate_robot_fn, est_grid_fn)
                p = gen_paths(robot_keypad, pos, robot_pos[button])
                for p in p:
                    next_code_paths.append(path + p)
            else:
                next_code_paths.append(path + [pos])
        code_paths = next_code_paths

    return map(lambda x: ''.join(path_to_dirs(x)), code_paths)
        

def subseqs(seq):
    try:
        i = 0
        while i < len(seq):
            j = seq.index('A', i)
            yield seq[i:j+1]
            i = j + 1
    except:
        pass



@functools.cache
def code_to_len(code, n):
    num_seqs = defaultdict(int)
    for seq in subseqs(code):
        num_seqs[seq] += 1

    for _ in range(n):
        # print(num_seqs)
        next_num_seqs = defaultdict(int)
        for seq, cnt in num_seqs.items():
            for next_seq in subseqs(seq_to_seq(seq)):
                next_num_seqs[next_seq] += cnt
        num_seqs = next_num_seqs

    # total_cost = functools.reduce(operator.add, num_seqs.values(), 0)
    # print(total_cost)
    # print({ k:v/total_cost for k,v in num_seqs.items()})

    r = 0
    for seq, cnt in num_seqs.items():
        r += cnt * len(seq)
    return r


def seq_len2(code):
    n = 25
    keypad,kw,kh = parse_grid('keypad.txt')

    options = list(get_seqs(code, keypad))
    best = math.inf
    for code in options:
        best = min(best, code_to_len(code, n))
    return best

def part2(filename):
    input = parse_file(filename)
    ans = 0

    global robot_keypad, robot_pos
    robot,rw,rh = parse_grid('robot.txt')
    robot_keypad = robot

    keypad_to_pos = {}
    for k,v in robot.items():
        keypad_to_pos[v] = k
    robot_pos = keypad_to_pos

    for button in ['<', '>', '^', 'v', 'A']:
        for path in gen_paths(robot_keypad, robot_pos['A'], robot_pos[button]):
            code = ''.join(path_to_dirs(path))
            print(button, path, ' -> ', code_to_len(code, 5))

    for code in input:
        seq_length = seq_len2(code)
        complexity = int(code[:-1])
        print(seq_length, complexity)
        ans += seq_length * complexity

    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

# 363680443427792 too high
# 142399336241600 too low
# 225887582184500 NO
# 223951999210460 NO
# 
# part2('example.txt')
part2('input.txt')
