import functools

from helpers import *


def flood_fill(m, pos):
    t = m[pos]
    area = set([pos])

    open = [pos]
    while len(open):
        p = open.pop()
        for n in neighbors(p):
            if n in m and m[n] == t and n not in area:
                area.add(n)
                open.append(n)

    return area


def get_garden_and_plots(filename):
    input,_,_ = parse_grid(filename)
    plots = []

    for pos in input.keys():
        if any(filter(lambda x: pos in x, plots)):
            continue
        plots.append(flood_fill(input, pos))

    return input, plots


def perimeter(m, plot):
    t = m[next(iter(plot))]
    perimeter = set()
    for p in plot:
        for dir in cardinals:
            n = vadd(dir, p)
            if n not in m or m[n] != t:
                perimeter.add((n, dir))

    return perimeter


def part1(filename):
    input,plots = get_garden_and_plots(filename)
    
    ans = functools.reduce(lambda acc, p: acc + len(p) * len(perimeter(input, p)), plots, 0)
    print(f'P1 {filename}: {ans}')


def adjacent(a, b):
    if mhn_dist(a[0], b[0]) == 1 and a[1] == b[1]:
        return True
    return False


def sides(m, plot):
    perim = sorted(perimeter(m, plot))
    sides = []

    for a in perim:
        if any(filter(lambda x: a in x, sides)):
            continue
        side = [a]
        for b in perim:
            if a == b:
                continue
            if adjacent(b, side[-1]):
                side.append(b)
        sides.append(set(side))
    return len(sides)


def part2(filename):
    input,plots = get_garden_and_plots(filename)

    ans = functools.reduce(lambda acc, p: acc + len(p) * sides(input, p), plots, 0)
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
