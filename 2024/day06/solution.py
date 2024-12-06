import functools

from helpers import *


def loops(m):
    guard_pos = [k for k,v in m.items() if v == '^'][0]
    dir = 'N'

    while True:
        if m[guard_pos] == dir:
            return True
        m[guard_pos] = dir
        n = vadd(dirs[dir], guard_pos)
        if n not in m:
            return False
        while m[n] == '#':
            dir = turn_right(dir)
            n = vadd(dirs[dir], guard_pos)
        guard_pos = n


def part1(filename):
    m,_,_ = parse_grid(filename)
    loops(m)

    ans = functools.reduce(lambda x,y: 1+x if y in turns else x, m.values(), 0)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    m,_,_ = parse_grid(filename)
    guard_pos = [k for k,v in m.items() if v == '^'][0]
    ans = 0

    initial_path = dict(m)
    loops(initial_path)

    for pos,v in initial_path.items():
        if v in turns and pos != guard_pos:
            c = dict(m)
            c[pos] = '#'
            if loops(c):
                ans += 1

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
