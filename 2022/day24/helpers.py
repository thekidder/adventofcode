import operator

def file(name):
    with open(name, 'r') as f:
        return f.read()


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
    '<': (-1, 0),
    '>': (1, 0),
    'v': (0, 1),
    '^': (0, -1),
}

to_dirs = {
    (-1, 0): '<',
    (1, 0): '>',
    (0, 1): 'v',
    (0, -1): '^',
}