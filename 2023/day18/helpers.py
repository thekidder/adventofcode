import operator

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


def print_grid(m, minx, miny, mx, my):
    for y in range(miny, my+1):
        for x in range(minx, mx+1):
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


dirs = {
    'L': (-1, 0),
    'R': (1, 0),
    'D': (0, 1),
    'U': (0, -1),
}


turns = ['L', 'U', 'R', 'D']
turn_lookup = dict(map(reversed, enumerate(turns)))


def turn_left(dir):
    return turns[(turn_lookup[dir] - 1) % 4]


def turn_right(dir):
    return turns[(turn_lookup[dir] + 1) % 4]
