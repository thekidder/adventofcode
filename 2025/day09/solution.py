import itertools
import random
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


def get_area(edges, input, a, b):
    min_x = min(a[0], b[0])
    max_x = max(a[0], b[0])
    min_y = min(a[1], b[1])
    max_y = max(a[1], b[1])

    corners = [
        (min_x+0.5, min_y+0.5),
        (max_x-0.5, min_y+0.5),
        (min_x+0.5, max_y-0.5),
        (max_x-0.5, max_y-0.5),
    ]

    # test_points = []
    # for i in range(1000):
    #     test_points.append(
    #         (random.uniform(min_x+0.5, max_x-0.5), random.uniform(min_y+0.5, max_y-0.5))
    #     )

    test_points = set()
    for x,y in input:
        for dir in all_directions:
            (x, y) = vadd((x, y), (dir[0]*0.5, dir[1]*0.5))
            if x <= min_x:
                x = min_x + 0.5
            elif x >= max_x:
                x = max_x - 0.5
            if y <= min_y:
                y = min_y + 0.5
            elif y >= max_y:
                y = max_y - 0.5
            test_points.add((x,y))
    for x,y in corners:
        test_points.add((x,y))

    for ray in test_points:
        edge_cnt = 0
        for edge in edges:
            if ray[0] < edge[0][0] and ray[1] > edge[0][1] and ray[1] < edge[1][1]:
                edge_cnt += 1
        if edge_cnt % 2 == 0:
            return 0
    return operator.mul(*vsub((max_x+1, max_y+1), (min_x, min_y)))



def part2(filename):
    input = parse_file(filename)

    edges = []
    for i, coord in enumerate(input):
        prev = input[i-1]
        dir = tuple(map(sign, vsub(coord, prev)))
        if dir[0] == 0:
            mi = min(prev, coord)
            ma = max(prev, coord)
            edges.append((mi, ma))

    # print(edges)

    ans = 0
    for a, b in itertools.combinations(input, 2):
        ans = max(get_area(edges, input, a, b), ans)
        # print(ans)

    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

part2('example.txt')
part2('input.txt') 

# 3944382296 too high 
# 3904033833 no
# 127710216 no
# 1649971048 ?
# 1749142296 ?
# 1750802724 ?
# 101621541 ?
# 1226 too low 
