import functools

from helpers import *

def score(m, pos):
    if m[pos] != 0:
        return (0,0)
    open_list = [pos]
    num_paths = 0
    ends = set()
    while len(open_list):
        p = open_list.pop()
        if m[p] == 9:
            num_paths += 1
            ends.add(p)
            continue
        val = m[p]
        for dir in cardinals:
            n = vadd(p, dir)
            if n in m and m[n] == val + 1:
                open_list.append(n)
    return len(ends), num_paths


def solve(filename):
    input,_,_ = parse_grid(filename)

    ans = functools.reduce(lambda acc, x: vadd(acc, score(input, x)), input.keys(), (0,0))
    print(f'P1 {filename}: {ans[0]}')
    print(f'P2 {filename}: {ans[1]}')


solve('example.txt')
solve('input.txt')
