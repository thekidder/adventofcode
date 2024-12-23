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
    for c in cardinals:
        yield vadd(c, coord)


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
