from collections import defaultdict

import functools
import operator

adjacencies = [(x,y) for x in range(-1,2) for y in range(-1,2) if y != 0 or x != 0]

def vadd(a, b):
    return tuple(map(operator.add, a, b))


def parse_file(filename):
    m = set()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for y,line in enumerate(lines):
            m.update(map(lambda x: (x,y,), [x for x,c in enumerate(line) if c == '#']))
        return m


def adjacent(m, pos):
    for x,y in adjacencies:
        npos = vadd(pos, (x,y))
        if npos in m: return True
    return False


def can_move(m, pos, dir):
    if dir[1] != 0:
        return all([vadd(pos, (x, dir[1])) not in m for x in range(-1, 2)])
    return all([vadd(pos, (dir[0], y)) not in m for y in range(-1, 2)])
 

def get_move(m, coord, dirs):
    if adjacent(m, coord):
        for d in dirs:
            if can_move(m, coord, d):
                return vadd(coord, d)
    return coord


def sim(m, rounds):
    dirs = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
    ]

    for round in range(rounds):
        proposals = defaultdict(int)
        actions = {}
        for space in m:
            actions[space] = get_move(m, space, dirs)
            if actions[space] != space:
                proposals[actions[space]] += 1

        n = set([prev if prev == next or proposals[next] > 1 else next for prev,next in actions.items()])

        if all(map(lambda x: x>1, proposals.values())):
            break
        m = n

        dirs.append(dirs.pop(0))
    return m, round+1


def solve(filename, rounds):
    m = parse_file(filename)
    m, total_rounds = sim(m, rounds)

    minb = list(functools.reduce(lambda a,b: map(min, a, b), m))
    maxb = list(functools.reduce(lambda a,b: map(max, a, b), m))

    ans = (maxb[0] - minb[0] + 1) * (maxb[1] - minb[1] + 1) - len(m)

    print(f'Sim {filename} for {total_rounds} rounds: {ans}')


solve('example.txt', 10)
solve('input.txt', 10)

solve('example.txt', 1000)
solve('input.txt', 1000)
