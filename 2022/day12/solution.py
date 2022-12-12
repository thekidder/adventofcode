import operator
import sys


def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        return lines.split('\n')


def find(map, symbol):
    for x in range(len(map[0])):
        for y in range(len(map)):
            if map[y][x] == symbol:
                return (x,y)


neighbors = [
    (-1,0),
    (1,0),
    (0,1),
    (0,-1),
]


def get(m, coord):
    x,y = coord
    if y >= 0 and y < len(m) and x >= 0 and x < len(m[0]):
        return m[y][x]
    return None


def candidates(m, coord):
    x = get(m, coord)
    if x == 'E':
        x = 'z'
    for dir in neighbors:
        n = tuple(map(operator.add, coord, dir))
        y = get(m, n)
        if y == 'S':
           y = 'a'

        if y is not None and ord(x) - ord(y) <= 1:
            yield n


def solve(filename):
    input = parse_file(filename)
    s = find(input, 'E')
    e = find(input, 'S')
    ans = sys.maxsize
    dist = {}
    options = [(s, 0)]
    while len(options) > 0:
        c, d = options.pop()

        for n in candidates(input, c):
            if n not in dist or dist[n] > d + 1:
                dist[n] = d + 1
                options.append((n, d+1))

    for c,v in dist.items():
        if get(input, c) == 'a' or get(input, c) == 'S':
            ans = min(ans, v)
    print(f'P1 {filename}: dist to E: {dist[e]}; dist to any a: {ans}')


solve('example.txt')
solve('input.txt')
