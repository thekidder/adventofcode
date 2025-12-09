from collections import defaultdict
import itertools
from helpers import *

def parse_file(filename):
    with open(filename, 'r') as f:
        return mapl(lambda x: tuple(map(int, x.split(','))), f.read().split('\n'))


def part1(filename):
    input = parse_file(filename)
    ans = 0

    for a, b in itertools.combinations(input, 2):
        mi = min(a,b)
        ma = max(a,b)
        area = operator.mul(*vsub(mi, vadd(ma, (1,1))))
        ans = max(area, ans)

    print(f'P1 {filename}: {ans}')


def flood_fill(grid, pos):
    cands = [pos]
    while len(cands):
        pos = cands.pop()
        if grid[pos] != '.':
            continue
        for dir in cardinals:
            cands.append(vadd(dir, pos))
        grid[pos] = 'X'


def get_area(grid, reverse_x, reverse_y, a, b):
    min_x = min(a[0], b[0])
    max_x = max(a[0], b[0])
    min_y = min(a[1], b[1])
    max_y = max(a[1], b[1])

    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if grid[(x,y)] == '.':
                return 0
            
    min_x = reverse_x[min_x]
    max_x = reverse_x[max_x]
    min_y = reverse_y[min_y]
    max_y = reverse_y[max_y]
    return operator.mul(*vsub((max_x+1, max_y+1), (min_x, min_y)))


def part2(filename):
    input = parse_file(filename)
    x_coords = set()
    y_coords = set()
    for coord in input:
        x_coords.add(coord[0])
        y_coords.add(coord[1])

    x_coords = sorted(x_coords)
    y_coords = sorted(y_coords)

    to_x = {}
    to_y = {}
    reverse_x = {}
    reverse_y = {}
    new_coord = {}
    sx = len(x_coords)
    sy = len(y_coords)
    for j, y in enumerate(y_coords):
        reverse_y[j] = y
        to_y[y] = j

    for i, x in enumerate(x_coords):
        reverse_x[i] = x
        to_x[x] = i

    for p in input:
        new_coord[p] = (to_x[p[0]],to_y[p[1]])

    grid = defaultdict(lambda: '.')
    fill_start = None
    for i,p in enumerate(input):
        prev = new_coord[input[i-1]]
        coord = new_coord[p]

        dir = tuple(map(sign, vsub(coord, prev)))
        prev = vadd(prev, dir)
        while prev != coord:
            grid[prev] = 'X'
            prev = vadd(prev, dir)

        grid[coord] = '#'
    
    for i,p in enumerate(input):
        prev_prev = new_coord[input[i-2]]
        prev = new_coord[input[i-1]]
        coord = new_coord[p]
        last_dir = tuple(map(sign, vsub(prev, prev_prev)))
        dir = tuple(map(sign, vsub(coord, prev)))
        if last_dir == (1, 0) and dir == (0, 1) and grid[fill_start] == '.':
            fill_start = vadd(prev, (-1, 1))

    flood_fill(grid, fill_start)
    print_grid(grid, sx, sy)

    ans = 0
    i = 0
    total = math.comb(len(input), 2)
    print(f'trying {total} combinations')
    for a, b in itertools.combinations(new_coord.values(), 2):
        # if i % 100 == 0:
        #     print(f'iteration {i}/{total}')
        area = get_area(grid, reverse_x, reverse_y, a, b)
        if area > ans:
            ans = area
            print(a, b, ans)
        i += 1

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

