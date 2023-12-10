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


def vadd(a, b):
    return tuple(map(operator.add, a, b))


dirs = {
    'W': (-1, 0),
    'E': (1, 0),
    'S': (0, 1),
    'N': (0, -1),
}