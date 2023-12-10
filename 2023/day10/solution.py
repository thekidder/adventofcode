from collections import defaultdict

from helpers import *


connections = {
    '7': set(['W', 'S']),
    'F': set(['E', 'S']),
    'J': set(['W', 'N']),
    'L': set(['E', 'N']),
    '-': set(['E', 'W']),
    '|': set(['N', 'S']),
    'S': set(['N', 'S', 'E', 'W'])
}


def connected_cells(m, coord):
    if coord not in m:
        return []
    if m[coord] == '.':
        return []
    return list(map(lambda dir: vadd(dirs[dir], coord), connections[m[coord]]))


def find_max_dists(m, src, dist, r):
    next = [(src, dist)]

    while len(next) > 0:
        src, dist = next.pop(0)
        neighbors = connected_cells(m, src)
        for coord in neighbors:
            if src not in connected_cells(m, coord):
                continue
            if dist + 1 < r[coord]:
                r[coord] = dist + 1

                next.append((coord, dist+1))


def part1(filename):
    input,mx,my = parse_grid(filename)
    for coord, v in input.items():
        if v != 'S':
            continue
        max_from_coord = defaultdict(lambda: float('inf'))
        max_from_coord[coord] = 0
        find_max_dists(input, coord, 0, max_from_coord)
    print(f'P1 {filename}: {max(max_from_coord.values())}')


ray_dir = (-1, 0)
def raycast(coord, pipes):
    cnt = 0
    while coord[0] > 0:
        coord = vadd(coord, ray_dir)
        if coord in pipes and pipes[coord] in ['7', '|', 'F']:
            cnt += 1
    return cnt


def part2(filename):
    input,mx,my = parse_grid(filename)
    pipe_costs = defaultdict(lambda: float('inf'))
    snake = None
    for coord, v in input.items():
        if v != 'S':
            continue
        snake = coord
        pipe_costs[coord] = 0
        find_max_dists(input, coord, 0, pipe_costs)

    pipes = {}
    for coord in pipe_costs:
        pipes[coord] = input[coord]

    # replace the snake with the proper right angle piece
    connected_to_snake = set()
    for dir in dirs.values():
        if snake in connected_cells(pipes, vadd(dir, snake)):
            connected_to_snake.add(dir)
    for joint,neighbors in connections.items():
        if len(set(map(lambda d: dirs[d], neighbors)) & connected_to_snake) == 2:
            pipes[snake] = joint
            break

    ans = 0
    print_grid(pipes,mx,my)
    for coord, v in input.items():
        if coord not in pipes and raycast(coord, pipes) % 2 == 1:
            ans += 1
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

# part2('example2.txt')
# part2('input.txt')
