from collections import defaultdict

from helpers import *
from intcode import *


def paint(code, squares):
    dir = 'N'
    coord = (0,0)

    def get_input():
        if coord in squares:
            return squares[coord]
        return 0

    prog = run(code, get_input, False)
    steps = 0

    while True:
        try:
            color = next(prog)
            squares[coord] = color
            turn = next(prog)
            if turn == 0:
                dir = turn_left(dir)
            else:
                dir = turn_right(dir)
            coord = vadd(coord, dirs[dir])
            steps += 1

            # print_grid(squares)
            # print(f'{color}, {turn} :: {coord}, {dir}, {len(squares.keys())}')
            # print()
        except StopIteration:
            break


def part1(filename):
    code = parse(file(filename))
    squares = defaultdict(int)
    paint(code, squares)

    ans = len(squares.keys())
    print(f'P1 {filename}: {ans}')


def part2(filename):
    code = parse(file(filename))
    squares = defaultdict(int)
    squares[(0,0)] = 1
    paint(code, squares)

    print_grid(squares)


part1('input.txt')
part2('input.txt')
