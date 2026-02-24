from collections import defaultdict

import functools
import operator
import heapq
import math
import sys


def print_problem(fn, input):
    if isinstance(input, str):
        if not input.endswith('.txt'):
            if len(input) > 20:
                input = input[:20] + '...'
        input = input.replace('\n', '')
    return f'{fn.__name__}({input}):'


def check(fn, input, expected, **kwargs):
    ans = exec(fn, input, log=False, **kwargs)
    if ans != expected:
        print(f'‼️ {print_problem(fn, input)} expected {expected}; got {ans}')
        sys.exit(1)
    print(f'✅ {print_problem(fn, input)} got {ans}')


def exec(fn, input, log=True, **kwargs):
    wrapper = None
    if isinstance(input, int):
        wrapper = functools.partial(fn, input, **kwargs)
    elif isinstance(input, str):
        if input.endswith('.txt'):
            with open(input, 'r') as f:
                input_txt = f.read()
                wrapper = functools.partial(fn, input_txt, **kwargs)
        else:
            # to make it easier to define input as multiline strings, strip input first
            wrapper = functools.partial(fn, input.strip())
    else:
        print(f'‼️ {print_problem(fn, input)} weird input type')
        sys.exit(2)
    ans = wrapper()
    if log:
        print(f'﹖ {print_problem(fn, input)} got {ans}')
    return ans


def parse_grid(text):
    r = {}
    mx = 0
    my = 0
    for (y, l) in enumerate(text.split('\n')):
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


def cardinal_neighbors(coord):
    for dir in cardinals:
        yield vadd(coord, dir)


def all_neighbors(coord):
    for xd in range(-1, 2):
        for yd in range(-1, 2):
            if xd == 0 and yd == 0:
                continue
            yield (coord[0] + xd, coord[1] + yd)


def sign(n):
    return (n > 0) - (n < 0)


def mapl(fn, itr):
    return list(map(fn, itr))


def vadd(a, b):
    return tuple(map(operator.add, a, b))


def vsub(a, b):
    return tuple(map(operator.sub, a, b))


def vmul(a, b):
    return tuple(map(operator.mul, a, b))


def sqr_dist(a, b):
    return sum(map(lambda x: x ** 2, vsub(a, b)))


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

dirs = {
    'W': (-1, 0),
    'E': (1, 0),
    'S': (0, 1),
    'N': (0, -1),
}

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


def a_star(
    context, # context includes all info necessary to build a path; the map or graph
    start_loc, # starting location
    end_loc, # end location
    generate_fn, # fn that takes context, cost, loc and generates an iterable of (cost, loc) tuples
    est_fn, # fn that takes in context, start, end and returns an estimate of cost. estimate must not overestimate cost
):
    open = []

    # internal state is a tuple of (cost + remaining_est, cost, loc)
    heapq.heappush(open, (0, 0, start_loc))

    best_costs = defaultdict(lambda: math.inf)
    came_from = {}

    while len(open):
        _, cost, loc  = heapq.heappop(open)
        if loc == end_loc:
            return cost, construct_path(came_from, start_loc, end_loc)
        for next_cost, next_loc in generate_fn(context, cost, loc):
            if next_cost < best_costs[next_loc]:
                best_costs[next_loc] = next_cost
                came_from[next_loc] = loc
                heapq.heappush(open, (est_fn(context, next_loc, end_loc) + next_cost, next_cost, next_loc))
    return None, None