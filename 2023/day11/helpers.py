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


def print_grid(m, mx, my):
    for y in range(my):
        for x in range(mx):
            print(m[(x,y)] if (x,y) in m else '.', end = '')
        print()


def vsub(a, b):
    return tuple(map(operator.sub, a, b))


def mhn_dist(a, b):
    return sum(map(abs, vsub(a, b)))
