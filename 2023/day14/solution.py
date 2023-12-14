from helpers import *

def roll(input, mx, my, dir):
    moves = 1
    while moves > 0:
        moves = 0
        for y in range(my+1):
            for x in range(mx+1):
                if input[(x,y)] != 'O':
                    continue
                n = vadd((x,y), dir)
                if n in input and input[n] == '.':
                    input[n] = 'O'
                    input[(x,y)] = '.'
                    moves += 1


def load(input, my):
    r = 0
    for (x,y), v in input.items():
        if v == 'O':
            r += my - y + 1 
    return r


def part1(filename):
    input,mx,my = parse_grid(filename)
    # print_grid(input,mx,my)
    # print()

    roll(input,mx,my, dirs['N'])
    print(f'P1 {filename}: {load(input,my)}')


def has_cycle(prev):
    # cycle len up to 100
    for i in range(2,100):
        if len(prev) < i * 2:
            continue

        if prev[-i:] == prev[-i*2:-i]:
            return i
    return 0

def part2(filename):
    input,mx,my = parse_grid(filename)
    # print_grid(input,mx,my)
    # print()

    i = 0
    prev = []
    while not has_cycle(prev):
        roll(input,mx,my, dirs['N'])
        roll(input,mx,my, dirs['W'])
        roll(input,mx,my, dirs['S'])
        roll(input,mx,my, dirs['E'])

        i += 1
        
        prev.append(load(input,my))
    cycle_len = has_cycle(prev)
    prev = prev[-cycle_len:]
    print(f'found cycle of len {cycle_len} after {i} iterations: {prev}')
    ans = prev[(1000000000 - i - 1) % cycle_len]
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
