import operator

def sign(n):
    return (n > 0) - (n < 0)


def vadd(a, b):
    return tuple(map(operator.add, a, b))


def vmul(a, b):
    return tuple(map(operator.add, a, b))


dirs = {
    'W': (-1, 0),
    'E': (1, 0),
    'S': (0, -1),
    'N': (0, 1),
}