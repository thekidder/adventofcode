from helpers import *

def part1(filename):
    input, sx, sy = parse_grid(filename)
    ans = 0

    for pos, x in input.items():
        if x == '@':
            adj = 0
            for dir in all_directions:
                npos = vadd(pos, dir)
                if npos in input and input[npos] == '@':
                    adj += 1
            if adj < 4:
                ans += 1

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input, sx, sy = parse_grid(filename)
    ans = 0

    grid = input
    changes = True
    # print_grid(grid, sx, sy)
    # print()
    while changes:
        changes = False
        next_grid = grid.copy()
        for pos, x in grid.items():
            if x == '@':
                adj = 0
                for dir in all_directions:
                    npos = vadd(pos, dir)
                    if npos in grid and grid[npos] == '@':
                        adj += 1
                if adj < 4:
                    changes = True
                    ans += 1
                    next_grid[pos] = '.'
        grid = next_grid
        # if changes:
        #     print_grid(grid, sx, sy)
        #     print()

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
