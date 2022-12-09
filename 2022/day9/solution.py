def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for l in f.readlines():
            d,n = l.split(' ')
            lines.append((d, int(n)))

        return lines


def sign(n):
    return (n > 0) - (n < 0)


def next(head, tail):
    dir = (tail[0] - head[0], tail[1] - head[1])
    if abs(dir[0]) > 1 or abs(dir[1]) > 1:
        return (tail[0] - sign(dir[0]), tail[1] - sign(dir[1]))
    return tail


dirs = {
    'U': (0,1),
    'D': (0,-1),
    'L': (-1,0),
    'R': (1,0),
}


def part1(filename):
    input = parse_file(filename)
    head = (0, 0)
    tail = (0, 0)
    visited = {(0,0): True}

    for dir,steps in input:
        d = dirs[dir]
        for i in range(steps):
            head = (head[0] + d[0], head[1] + d[1])
            tail = next(head, tail)
            visited[tail] = True

    print(f'P1 {filename}: {len(visited)}')


def part2(filename):
    input = parse_file(filename)
    knots = [(0,0)]*10
    visited = {(0,0): True}

    for dir,steps in input:
        d = dirs[dir]
        for i in range(steps):
            knots[0] = (knots[0][0] + d[0], knots[0][1] + d[1])
            for i in range(1, len(knots), 1):
                knots[i] = next(knots[i-1], knots[i])
            visited[knots[-1]] = True
    print(f'P2 {filename}: {len(visited)}')


part1('example.txt')
part1('input.txt')

part2('example2.txt')
part2('input.txt')
