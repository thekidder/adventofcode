from helpers import *

def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        grid, movements = lines.split('\n\n')
        grid,w,h = parse_grid(grid)
        movements = movements.replace('\n', '')

        return grid, w, h, movements


def parse_file2(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        grid, movements = lines.split('\n\n')
        grid,w,h = parse_grid2(grid)
        movements = movements.replace('\n', '')

        return grid, w, h, movements


def move_dep(grid, pos, dir):
    open = [pos]
    all_boxes = set()

    def add(p):
        open.append(vadd(p, dir))
        all_boxes.add(p)

    while len(open):
        pos = open.pop()
        if pos in all_boxes:
            continue
        v = grid[pos]
        if v == 'O':
            add(pos)
        elif v == '[':
            add(pos)
            add((pos[0]+1, pos[1]))
        elif v == ']':
            add(pos)
            add((pos[0]-1, pos[1]))
        elif v == '#':
            return False, []
    return True, list(all_boxes)


def sim(grid, pos, dir):
    dir = dirs[dir]
    n = vadd(pos, dir)
    can_move, deps = move_dep(grid, n, dir)
    if can_move:
        if dir == (-1, 0):
            deps.sort()
        elif dir == (1, 0):
            deps = reversed(sorted(deps))
        elif dir == (0, -1):
            deps = sorted(deps, key=lambda p: p[1])
        elif dir == (0, 1):
            deps = reversed(sorted(deps, key=lambda p: p[1]))
        for p in deps:
            grid[vadd(p, dir)] = grid[p]
            grid[p] = '.'

        grid[pos] = '.'
        grid[n] = '@'
        return n
    else:
        return pos


def solve(filename, parse_fn, part):
    grid, w, h, movements = parse_fn(filename)
    p = [k for k,v in grid.items() if v == '@'][0]

    for i in range(len(movements)):
        # print('')
        # print(f'Move {movements[i]}')
        p = sim(grid, p, movements[i])
        # print_grid(grid, w, h)

    ans = 0
    for p, v in grid.items():
        if v == '[' or v == 'O':
            ans += 100 * p[1] + p[0]
    print(f'{part} {filename}: {ans}')


solve('example.txt', parse_file, 'P1')
solve('input.txt', parse_file, 'P1')

solve('example.txt', parse_file2, 'P2')
solve('input.txt', parse_file2, 'P2')
