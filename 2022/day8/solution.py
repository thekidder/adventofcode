dirs = [
    (1, 0),
    (-1, 0),
    (0, -1),
    (0, 1),
]

def get(trees, coord):
    x,y = coord
    if x < 0 or x >= len(trees[0]) or y < 0 or y >= len(trees):
        return None
    return trees[y][x]


def next(coord, dir):
    return (coord[0]+dir[0],coord[1]+dir[1])


def visible(trees, coord, dir):
    h = get(trees, coord)
    while get(trees, next(coord, dir)) is not None:
        if get(trees, next(coord, dir)) >= h:
            return False
        coord = next(coord, dir)
    return True


def scenic(trees, coord, dir):
    h = get(trees, coord)
    cnt = 0
    while get(trees, next(coord, dir)) is not None:
        cnt += 1
        if get(trees, next(coord, dir)) >= h:
            break
        coord = next(coord, dir)
    return cnt


def parse_file(filename):
    trees = []
    with open(filename, 'r') as f:
        for line in f:
            row = []
            for t in line.strip():
                row.append(int(t))
            trees.append(row)
            
        return trees


def part1(filename):
    input = parse_file(filename)
    ans = 0
    for x in range(len(input[0])):
        for y in range(len(input)):
            for dir in dirs:
                if visible(input, (x,y), dir):
                    ans += 1
                    break
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    ans = 0
    for x in range(len(input[0])):
        for y in range(len(input)):
            s = 1
            for dir in dirs:
                s *= scenic(input, (x,y), dir)
            if s > ans:
                ans = s
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
