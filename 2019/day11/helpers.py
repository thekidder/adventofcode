import operator

def file(name):
    with open(name, 'r') as f:
        return f.read()


def print_grid(m):
    minx = min(map(lambda c: c[0], m.keys()))
    mx = max(map(lambda c: c[0], m.keys()))

    miny = min(map(lambda c: c[1], m.keys()))
    my = max(map(lambda c: c[1], m.keys()))

    for y in range(miny, my+1):
        for x in range(minx, mx+1):
            # print(m[(x,y)] if (x,y) in m else '.', end = '')
            print('#' if (x,y) in m and m[(x,y)] > 0 else ' ', end = '')
        print()


def vadd(a, b):
    return tuple(map(operator.add, a, b))


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
