from helpers import *


def part1(filename):
    input,sx,sy = parse_grid(filename)

    start = [k for k,v in input.items() if v == 'S'][0]
    end = [k for k,v in input.items() if v == 'E'][0]
    input[start] = '.'
    input[end] = '.'
    _,path = a_star(input, start, end, generate_grid_fn, est_grid_fn)

    ans = 0
    for i,loc in enumerate(path):
        for dir in cardinals:
            adj = vadd(loc, dir)
            adj2 = vadd(adj, dir)
            
            if adj in input and input[adj] == '#':
                try:
                    j = path.index(adj2)
                    if j - i - 2 >= 100:
                        ans += 1
                except:
                    pass

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input,sx,sy = parse_grid(filename)

    start = [k for k,v in input.items() if v == 'S'][0]
    end = [k for k,v in input.items() if v == 'E'][0]
    input[start] = '.'
    input[end] = '.'
    _,path = a_star(input, start, end, generate_grid_fn, est_grid_fn)

    ans = 0
    for i,loc in enumerate(path):
        for j in range(i + 4, len(path)):
            cheat_len = mhn_dist(loc, path[j])
            if cheat_len > 20:
                continue
            if (j - i) - cheat_len >= 100:
                ans += 1
    
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
