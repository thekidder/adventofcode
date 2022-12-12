import operator
import sys


def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        return list(map(list, lines.split('\n')))


def find(map, symbol):
    for x in range(len(map[0])):
        for y in range(len(map)):
            if map[y][x] == symbol:
                return (x,y)


def get(m, coord):
    x,y = coord
    if y >= 0 and y < len(m) and x >= 0 and x < len(m[0]):
        return m[y][x]
    return None


neighbors = [(-1,0),(1,0),(0,1),(0,-1)]
def candidates(m, coord):
    x = get(m, coord)
    for dir in neighbors:
        n = tuple(map(operator.add, coord, dir))
        y = get(m, n)
        if y is not None and ord(x) - ord(y) <= 1:
            yield n


def solve(filename):
    input = parse_file(filename)
    start = find(input, 'S')
    end = find(input, 'E')
    input[start[1]][start[0]] = 'a'
    input[end[1]][end[0]] = 'z'
    distances_from_end = {}
    # queue is of coord, num_steps
    queue = [(end, 0)]
    while len(queue) > 0:
        c, d = queue.pop(0)
        d += 1
        for n in candidates(input, c):
            if n not in distances_from_end or distances_from_end[n] > d:
                distances_from_end[n] = d
                queue.append((n, d))

    ans = sys.maxsize
    for c,v in distances_from_end.items():
        if get(input, c) == 'a':
            ans = min(ans, v)
    print(f'P1 {filename}: dist to E: {distances_from_end[start]}; dist to any a: {ans}')


solve('example.txt')
solve('input.txt')
