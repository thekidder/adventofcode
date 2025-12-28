import copy

from intcode import *
from helpers import *

def get_beam(memory, pos):
    i = 0
    def get_input():
        nonlocal i
        v = pos[i]
        i += 1
        return v
    return next(run(copy.copy(memory), get_input, False))


def part1(data):
    ans = 0
    memory = parse(data)
    for x in range(50):
        for y in range(50):
            ans += get_beam(memory, (x, y))
    return ans


def get_slope(memory):
    for x in range(4):
        for y in range(4):
            pos = (x, y)
            if (x != 0 or y != 0) and get_beam(memory, pos):
                return pos


def fits_beam(memory, pos):
    x,y = pos
    return get_beam(memory, (x,y)) and \
        get_beam(memory, (x+99,y)) and \
        get_beam(memory, (x,y+99)) and \
        get_beam(memory, (x+99,y+99))


def part2(data):
    memory = parse(data)
    slope = get_slope(memory)
    slope = slope[0] / slope[1]
    for y in range(100000):
        x = int(slope * y)
        while x > 0 and get_beam(memory, (x,y)):
            x-= 1
        x += 1
        if y - 99 >= 0 and fits_beam(memory, (x, y-99)):
            return x * 10000 + y - 99


exec(part1, 'input.txt')
exec(part2, 'input.txt')
