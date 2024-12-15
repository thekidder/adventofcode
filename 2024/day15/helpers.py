import operator

def file(name):
    with open(name, 'r') as f:
        return f.read()


def parse_grid(f):
    r = {}
    mx = 0
    my = 0
    for (y, l) in enumerate(f.split('\n')):
        my = y
        for (x, c) in enumerate(l.strip()):
            r[(x,y)] = c
            mx = x

    return r,mx,my


def parse_grid2(f):
    r = {}
    mx = 0
    x = 0
    my = 0
    for (y, l) in enumerate(f.split('\n')):
        my = y
        x = 0
        for c in l.strip():
            if c == 'O':
                r[(x,y)] = '['
                r[(x+1,y)] = ']'
                x += 2
            elif c == '@':
                r[(x,y)] = '@'
                r[(x+1,y)] = '.'
                x += 2
            else:
                r[(x,y)] = c
                r[(x+1,y)] = c
                x += 2
            mx = x

    return r,mx-1,my


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

dirs = {
    '<': (-1, 0),
    '>': (1, 0),
    'v': (0, 1),
    '^': (0, -1),
}

turns = ['W', 'N', 'E', 'S']
turn_lookup = dict(map(reversed, enumerate(turns)))

def turn_left(dir):
    return turns[(turn_lookup[dir] - 1) % 4]


def turn_right(dir):
    return turns[(turn_lookup[dir] + 1) % 4]
