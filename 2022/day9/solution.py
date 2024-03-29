import operator

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
    dir = tuple(map(operator.sub, head, tail))
    if any(map(lambda x: abs(x)>1, dir)):
        return tuple(map(operator.add, tail, map(sign, dir)))
    return tail


dirs = {
    'U': (0,1),
    'D': (0,-1),
    'L': (-1,0),
    'R': (1,0),
}


def solve(filename, num_knots):
    input = parse_file(filename)
    knots = [(0,0)]*num_knots
    visited = {(0,0): True}

    for dir,steps in input:
        d = dirs[dir]
        for i in range(steps):
            knots[0] = (knots[0][0] + d[0], knots[0][1] + d[1])
            for i in range(1, len(knots), 1):
                knots[i] = next(knots[i-1], knots[i])
            visited[knots[-1]] = True
    print(f'P2 {filename}: {len(visited)}')


solve('example.txt', 2)
solve('input.txt', 2)

solve('example2.txt', 10)
solve('input.txt', 10)
