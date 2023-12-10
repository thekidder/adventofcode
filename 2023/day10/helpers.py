import operator

def file(name):
    with open(name, 'r') as f:
        return f.read()


def parse_grid(filename):
    r = {}
    with open(filename, 'r') as f:
        for (y, l) in enumerate(f):
            for (x, c) in enumerate(l.strip()):
                r[(x,y)] = c

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
    return tuple(map(operator.add, a, b))


def mhn_dist(a, b):
    return sum(map(abs, vsub(a, b)))

dirs = {
    'W': (-1, 0),
    'E': (1, 0),
    'S': (0, 1),
    'N': (0, -1),
}