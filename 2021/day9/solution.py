import functools

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append([h for h in map(int, line.strip())])

    return lines


def neighbors(lines, pos):
    x,y = pos
    if x > 0:
        yield (x-1,y)
    if x < len(lines[0]) - 1:
        yield (x+1,y)
    if y > 0:
        yield (x,y-1)
    if y < len(lines) - 1:
        yield (x,y+1)


def get_val(lines, pos):
    return lines[pos[1]][pos[0]]


def flood(lines, initial_pos):
    open = set()
    open.add(initial_pos)
    closed = set()

    while len(open) > 0:
        pos = open.pop()
        closed.add(pos)

        last = get_val(lines, pos)

        for n in neighbors(lines, pos):
            val = get_val(lines, n)
            if val == 9 or val <= last:
                continue
            if n not in closed:
                open.add(n)

    return len(closed)


def part1(filename):
    ans = 0
    lines = parse_file(filename)
    for y, line in enumerate(lines):
        for x, h in enumerate(line):
            if all(map(lambda pos: get_val(lines, pos) > h, neighbors(lines, (x, y)))):
                ans += h + 1 
    print(f'ANSWER: {ans}')


def part2(filename):
    lines = parse_file(filename)
    low_points = []
    for y, line in enumerate(lines):
        for x, h in enumerate(line):
            if all(map(lambda pos: get_val(lines, pos) > h, neighbors(lines, (x, y)))):
                low_points.append((x,y))

    sizes = sorted([flood(lines, p) for p in low_points])
    ans = functools.reduce(lambda x,y:x*y, sizes[-3:], 1)

    print(f'ANSWER: {ans}')


part2('input.txt')
