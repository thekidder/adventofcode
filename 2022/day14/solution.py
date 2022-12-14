def sign(n):
    return (n > 0) - (n < 0)


def parse_file(filename):
    r = {}
    max_y = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        for l in lines:
            coords = list([[int(x) for x in x.split(',')] for x in l.split('->')])
            for i in range(1, len(coords)):
                prev_x, prev_y = coords[i-1]
                x, y = coords[i]
                r[(prev_x, prev_y)] = True
                while prev_x != x or prev_y != y:
                    prev_x += sign(x - prev_x)
                    prev_y += sign(y - prev_y)
                    max_y = max(prev_y, max_y)
                    r[(prev_x, prev_y)] = True

        return r, max_y


def falls_to(c):
    yield (c[0], c[1]+1)
    yield (c[0]-1, c[1]+1)
    yield (c[0]+1, c[1]+1)


def step(m, coord, max_y):
    def valid(coord):
        return coord not in m and coord[1] <= max_y
    return next(filter(valid, falls_to(coord)), None)


def simulate(m, coord, max_y, floor):
    while coord is not None:
        prev = coord
        coord = step(m, prev, max_y)
    if not floor and prev[1] == max_y:
        return 0
    if prev not in m:
        m[prev] = True
        return 1
    return 0


# def simulate(m, src, max_y, floor):
#     coord = sim(m, src, max_y)
    


def part1(filename):
    m,max_y = parse_file(filename)
    ans = 0
    while simulate(m, (500, 0), max_y, False):
        ans += 1
    print(f'P1 {filename}: {ans}')
    

def part2(filename):
    m,max_y = parse_file(filename)
    ans = 0
    while simulate(m, (500, 0), max_y+1, True):
        ans += 1
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
