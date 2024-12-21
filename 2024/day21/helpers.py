from collections import defaultdict

import operator
import heapq
import math


def file(name):
    with open(name, 'r') as f:
        return f.read()


def parse_grid(filename):
    r = {}
    mx = 0
    my = 0
    with open(filename, 'r') as f:
        for (y, l) in enumerate(f):
            my = y
            for (x, c) in enumerate(l.strip()):
                r[(x,y)] = c
                mx = x

        return r,mx,my


def print_grid(m, mx, my):
    for y in range(my+1):
        for x in range(mx+1):
            print(m[(x,y)] if (x,y) in m else '.', end = '')
        print()


def transpose(m):
    r = {}
    for (x,y), v in m.items():
        r[(y,x)] = v
    return r


def neighbors(coord):
    for xd in range(-1, 2):
        for yd in range(-1, 2):
            if xd == 0 and yd == 0:
                continue
            yield (coord[0] + xd, coord[1] + yd)


def sign(n):
    return (n > 0) - (n < 0)


def vadd(a, b):
    return tuple(map(operator.add, a, b))


def vsub(a, b):
    return tuple(map(operator.sub, a, b))


def vmul(a, b):
    return tuple(map(operator.mul, a, b))


def mhn_dist(a, b):
    return sum(map(abs, vsub(a, b)))


def vneg(a):
    return tuple(map(operator.neg, a))


# various useful representations for directions
cardinals = [
    (-1, 0),
    ( 1, 0),
    ( 0,-1),
    ( 0, 1),
]

diagonals = [
    (-1,-1),
    ( 1,-1),
    (-1, 1),
    ( 1, 1),
]

all_directions = cardinals + diagonals


turns = ['W', 'N', 'E', 'S']
turn_lookup = dict(map(reversed, enumerate(turns)))

def turn_left(dir):
    return turns[(turn_lookup[dir] - 1) % 4]


def turn_right(dir):
    return turns[(turn_lookup[dir] + 1) % 4]


# a star helpers
def construct_path(came_from, start_loc, end_loc):
    path = [end_loc]
    loc = end_loc
    while True:
        path.append(came_from[loc])
        loc = path[-1]
        if loc == start_loc:
            break
    path.reverse()
    return path


def est_grid_fn(_, start, end):
    return mhn_dist(start, end)


def generate_neg_grid_fn(grid, cost, loc):
    for dir in cardinals:
        n = vadd(loc, dir)
        if n in grid and grid[n] == '#':
            yield (cost + 1, n)


def generate_grid_fn(grid, cost, loc):
    for dir in cardinals:
        n = vadd(loc, dir)
        if n in grid and grid[n] == '.':
            yield (cost + 1, n)


def construct_all_paths(came_from, start_loc, end_loc):
    paths = []
    path_candidates = [[end_loc]]
    while len(path_candidates):
        p = path_candidates.pop()
        ps = []
        for n in came_from[p[-1]]:
            if mhn_dist(n, start_loc) < mhn_dist(p[-1], start_loc):
                ps.append(p[:] + [n])
        for p in ps:
            if p[-1] == start_loc:
                paths.append(p)
            else:
                path_candidates.append(p)
    return list(map(lambda x: list(reversed(x)), paths))


def a_star(
    context, # context includes all info necessary to build a path; the map or graph
    start_loc, # starting location
    end_loc, # end location
    generate_fn, # fn that takes context, cost, loc and generates an iterable of (cost, loc) tuples
    est_fn, # fn that takes in context, start, end and returns an estimate of cost. estimate must not overestimate cost
):
    open = []
    closed = set()

    # internal state is a tuple of (cost + remaining_est, cost, loc)
    heapq.heappush(open, (0, 0, start_loc))

    best_costs = defaultdict(lambda: math.inf)
    came_from = defaultdict(set)

    while len(open):
        _, cost, loc  = heapq.heappop(open)
        # print(loc, end_loc)
        if loc == end_loc:
            continue
        for next_cost, next_loc in generate_fn(context, cost, loc):
            if next_cost <= best_costs[next_loc] and (next_cost, next_loc, loc) not in closed:
                closed.add((next_cost, next_loc, loc))
                best_costs[next_loc] = next_cost
                came_from[next_loc].add(loc)
                heapq.heappush(open, (est_fn(context, next_loc, end_loc) + next_cost, next_cost, next_loc))
    return best_costs[end_loc], construct_all_paths(came_from, start_loc, end_loc)