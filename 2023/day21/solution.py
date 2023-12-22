import fractions
import math

from helpers import *


def is_plot(input,mx,my,c):
    c_m = (c[0] % (mx+1), c[1] % (my+1))
    return input[c_m] == '.'

def step(input, mx,my,locs):
    n = set()
    for l in locs:
        for d in dirs.values():
            c = vadd(d, l)
            if is_plot(input, mx, my, c):
                n.add(c)
    return n


def part1(filename, steps):
    input,mx,my = parse_grid(filename)
    for c,v in input.items():
        if v == 'S':
            start = c
            break
    input[start] = '.'
    # print_grid(input,mx,my)
    # print(start)

    locs = set([start])
    for _ in range(steps):
        locs = step(input, mx,my,locs)

    ans = len(locs)
    print(f'P1 {filename}: {ans}')


def poly_lagrange(p, x, y):
    a = (
        fractions.Fraction(
            math.prod(p - xj for xj in x if xj != xi),
            math.prod(xi - xj for xj in x if xj != xi),
        )
        for xi in x
    )
    return sum(ai * yi for ai, yi in zip(a, y))

def part2(filename):
    input,mx,my = parse_grid(filename)
    for c,v in input.items():
        if v == 'S':
            start = c
            break
    input[start] = '.'
    # print_grid(input,mx,my)
    # print(start)
    
    locs = set([start])
    for _ in range(65):
        locs = step(input, mx,my,locs)
    a = len(locs)
    print(a)
    for _ in range(131):
        locs = step(input, mx,my,locs)
    b = len(locs)
    print(b)
    for _ in range(131):
        locs = step(input, mx,my,locs)
    c = len(locs)
    print(c)

    x = [65, 131+65, 131+131+65]
    y =[a,b,c]
    ans= poly_lagrange(26501365,x,y)

    print(f'P2 {filename}: {ans} {int(ans)}')


# part1('example.txt', 6)
# part1('input.txt', 64)

# too low: 595147788145825
part2('input.txt')
