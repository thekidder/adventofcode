from collections import defaultdict

from helpers import *

def parse_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def wind_generator(pattern):
    winds = {
        '<': (-1, 0),
        '>': (1, 0)
    }
    pos = 0
    def gen():
        nonlocal pos
        r = pattern[pos]
        pos += 1
        pos %= len(pattern)
        return winds[r]
    return gen


heights = [1, 3, 3, 4, 2]

def rock_generator():
    rocks = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 2), (0, 1), (1, 1), (2, 1), (1, 0)],
        [(2, 2), (2, 1), (0, 0), (1, 0), (2, 0)],
        [(0, 3), (0, 2), (0, 1), (0, 0)],
        [(0, 1), (1, 1), (0, 0), (1, 0)],
    ]
    pos = 0
    def gen():
        nonlocal pos
        r = rocks[pos]
        pos += 1
        pos %= len(rocks)
        return r
    return gen


def collides(r, v, m):
    for coord in r:
        c = vadd(coord, v)
        if m[c] == True or c[0] < 0 or c[0] > 6:
            return True
    return False


def move(r, v):
    s = []
    for coord in r:
        s.append(vadd(coord, v))
    return s


def printm(m, max_y):
    for y in range(max_y, -1, -1):
        for x in range(0, 7):
            if m[(x,y)]:
                if y == 0:
                    print('@', end='')
                else:
                    print('#', end='')
            else:
                print('.', end='')
        print()


down = (0, -1)

def solve(filename, iterations):
    input = parse_file(filename)
    get_wind = wind_generator(input)
    get_rock = rock_generator()
    m = defaultdict(lambda: False, {(i,0):True for i in range(7)})
    max_y = 0

    buf = []
    cycle_len = len(input) * 5
    max_offset = 2000
    buf_len = None
    i = 0
    number_of_wind_pushes = 0

    while buf_len is None or i < buf_len * 3:
        i += 1
        resting = False
        r = move(get_rock(), (2, max_y+4))
        falls = 0
        while not resting:
            w = get_wind()
            if not collides(r, w, m):
                r = move(r, w)

            if not collides(r, down, m):
                r = move(r, down)
                falls += 1
            else:
                resting = True
                for coord in r:
                    max_y = max(max_y, coord[1])
                    m[coord] = True

        if i > max_offset:
            number_of_wind_pushes += falls + 1
        if buf_len is None and number_of_wind_pushes >= cycle_len:
            print(f'Found buffer len: {number_of_wind_pushes} {cycle_len} {i - max_offset}')
            buf_len = i - max_offset
        buf.append(falls)

    for offset in range(buf_len // 2):
        if all(map(lambda i: buf[offset + i] == buf[offset + i + buf_len], range(buf_len))):
            print(f'Found offset: {offset}')
            break

    initial = buf[:offset]
    buf = buf[offset:buf_len+offset]

    y = sum(map(lambda i:  max(0, (4 - initial[i]) + heights[i % 5]-1), range(offset)))

    final_buf = [max(0, (4 - buf[i % buf_len]) + heights[i % 5]-1) for i in range(buf_len * 5)]

    iterations -= offset
    y += sum(final_buf) * (iterations // len(final_buf))
    y += sum(final_buf[:iterations % len(final_buf)])

    print(f'Final height of {filename} after {iterations+offset} rocks: {y}')


solve('example.txt', 2022)
solve('input.txt', 2022)

solve('example.txt', 1000000000000)
solve('input.txt', 1000000000000)
