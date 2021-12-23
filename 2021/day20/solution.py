import functools
from itertools import product
import itertools

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        enhancement = [1 if c == '#' else 0 for c in f.readline().strip()]
        f.readline()
        for line in f:
            lines.append([1 if c == '#' else 0 for c in line.strip()])

    return enhancement, lines


def printgrid(grid):
    for line in grid:
        for c in line:
            print('#' if c == 1 else '.', end = '')
        print()


def region(grid, pos, bounds):
    for dir in product(range(-1,2),repeat=2):
        x = dir[1] + pos[0]
        y = dir[0] + pos[1]
        if x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
            yield grid[y][x]
        else:
            yield bounds


def region_index(grid, pos, bounds):
    ind = 0
    for bit in region(grid, pos, bounds):
        ind <<= 1
        ind |= bit
    return ind


def enhance(enhancement, grid, bounds):
    output = []
    for _ in range(len(grid)+2):
        output.append([0] * (len(grid[0])+2))

    for y in range(len(output)):
        for x in range(len(output[0])):
            pos = (x-1,y-1)
            ind = region_index(grid, pos, bounds)
            output[y][x] = enhancement[ind]

    if bounds == 0:
        bounds = enhancement[0]
    else:
        bounds = enhancement[511] 

    return output, bounds


def count(grid):
    ans = 0
    for line in grid:
        ans += functools.reduce(lambda x,y:x+y, line, 0)
    return ans


def part1(filename):
    enhancement,grid = parse_file(filename)
    bounds = 0
    grid, bounds = enhance(enhancement, grid, bounds)
    grid, bounds = enhance(enhancement, grid, bounds)
    print(f'ANSWER: {count(grid)}')


def part2(filename):
    enhancement,grid = parse_file(filename)
    bounds = 0
    for _ in range(50):
        grid, bounds = enhance(enhancement, grid, bounds)
    print(f'ANSWER: {count(grid)}')

part2('example.txt')
part2('input.txt')
