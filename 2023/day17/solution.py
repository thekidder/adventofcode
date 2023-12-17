from collections import defaultdict
from queue import PriorityQueue

from helpers import *


def valid(coord,mx,my):
    if coord[0] < 0 or coord[1] < 0:
        return False
    if coord[0] > mx or coord[1] > my:
        return False
    return True


def next(n,input,end,mx,my):
    if n[4] < 10:
        dir = n[3]
        nc = vadd(dirs[dir], n[2])
        if valid(nc,mx,my):
            yield (n[1]+mhn_dist(nc, end), n[1]+input[nc], nc, n[3], n[4]+1, n[2])

    if n[4] >= 4:
        dir = turn_left(n[3])
        nc = vadd(dirs[dir], n[2])
        if valid(nc,mx,my):
            yield (n[1]+mhn_dist(nc, end), n[1]+input[nc], nc, dir, 1, n[2])

        dir = turn_right(n[3])
        nc = vadd(dirs[dir], n[2])
        if valid(nc,mx,my):
            yield (n[1]+mhn_dist(nc, end), n[1]+input[nc], nc, dir, 1, n[2])


def astar(input,mx,my):
    # queue of elements of the form:
    # (estimate, cost, coord, dir, blocks_travled_in_dir, prev_coord)
    q = PriorityQueue()
    start = (0,0)
    end = (mx,my)
    q.put((mhn_dist(start, end), 0, start, 'E', 0, None))
    cnt = 0
    # map of (coord, dir, blocks_in_dir) -> lowest score
    scores = defaultdict(lambda: float('inf'))
    while q and cnt < 10000000:
        n = q.get()
        # print(n)
        if n[2] == end:
            print(cnt)
            return n[1]
        for ne in next(n, input, end, mx, my):
            score_key = (ne[2], ne[3], ne[4])
            if ne[1] < scores[score_key]:
                scores[score_key] = ne[1]
                q.put(ne)
        cnt += 1


def part1(filename):
    input,mx,my = parse_grid(filename)
    # print_grid(input,mx,my)
    ans = astar(input,mx,my)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input,mx,my = parse_grid(filename)
    print_grid(input,mx,my)
    ans = 0
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
part1('input.txt')

# part2('example.txt')
# part2('input.txt')
