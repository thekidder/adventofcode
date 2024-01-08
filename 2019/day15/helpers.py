import operator

from collections import defaultdict
from queue import PriorityQueue

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


def print_grid(m):
    minx = min(map(lambda x: x[0], m.keys()))
    miny = min(map(lambda x: x[1], m.keys()))

    maxx = max(map(lambda x: x[0], m.keys()))
    maxy = max(map(lambda x: x[1], m.keys()))
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            print(m[(x,y)] if (x,y) in m else ' ', end = '')
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


dirs = {
    3: (-1, 0),
    4: (1, 0),
    2: (0, 1),
    1: (0, -1),
}

inverse = {
    3: 4,
    4: 3,
    2: 1,
    1: 2,
}


turns = ['W', 'N', 'E', 'S']
turn_lookup = dict(map(reversed, enumerate(turns)))


def turn_left(dir):
    return turns[(turn_lookup[dir] - 1) % 4]


def turn_right(dir):
    return turns[(turn_lookup[dir] + 1) % 4]


def a_star(cost_fn, est_fn, neighbors_fn, start_node, end_node):
    # queue of elements of the form:
    # (estimate, cost, node, prev_node)
    q = PriorityQueue()
    q.put((est_fn(start_node, end_node), 0, start_node, []))
    cnt = 0
    # map of node -> lowest score
    scores = defaultdict(lambda: float('inf'))
    while q and cnt < 10000000:
        x = q.get()
        _,cost,node,path = x
        if node == end_node:
            return cost, path
        for next_node in neighbors_fn(node):
            next_cost = cost_fn(node, next_node)
            if cost+next_cost < scores[next_node]:
                scores[next_node] = next_cost
                q.put((est_fn(next_node, end_node), cost+next_cost, next_node, path + [next_node]))
        cnt += 1
    print(f'ERR: NO PATH FOUND')
    return None, None

