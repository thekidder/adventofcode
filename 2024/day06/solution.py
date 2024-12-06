import functools

from helpers import *


def part1(filename):
    m,sx,sy = parse_grid(filename)
    guard_pos = [k for k,v in m.items() if v == '^'][0]
    dir = 'N'

    while guard_pos in m:
        print(guard_pos)
        m[guard_pos] = 'X'
        n = vadd(dirs[dir], guard_pos)
        if n not in m:
            guard_pos = n
            continue
        if m[n] == '#':
            dir = turn_right(dir)
            n = vadd(dirs[dir], guard_pos)
        guard_pos = n


    ans = functools.reduce(lambda y,x: 1+y if x == 'X' else y, m.values(), 0)
    print(f'P1 {filename}: {ans}')


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



def part2(filename):
    m,sx,sy = parse_grid(filename)
    ans = 0
    for pos,v in m.items():
        if v == '.':
            c = dict(m)
            c[pos] = '#'
            if loops(c):
                ans += 1

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
