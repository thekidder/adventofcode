from collections import defaultdict

import functools
import operator

dirs = {
    '<': (-1, 0),
    '>': (1, 0),
    'v': (0, 1),
    '^': (0, -1),
}

to_dirs = {v:k for k,v in dirs.items()}

def vadd(a, b):
    return tuple(map(operator.add, a, b))


def parse_file(filename):
    m = defaultdict(list)
    with open(filename, 'r') as f:
        lines = f.readlines()
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                if c == '#':
                    # pass
                    m[(x,y)] = None
                elif c == '.':
                    pass
                    m[(x,y)] = []
                else:
                    m[(x,y)] = [dirs[c]]

        bounds = list(functools.reduce(lambda a,b: map(max, a, b), m.keys()))

        start = (next(filter(lambda x: m[(x, 0)] == [], range(bounds[0]+1))), 0)
        end = (next(filter(lambda x: m[(x, bounds[1])] == [], range(bounds[0]+1))), bounds[1])

        return m, bounds, start, end


def next_blizzard(m, bounds, pos, dir):
    if dir == (-1,0) and pos[0] == 1:
        return (bounds[0]-1, pos[1])
    if dir == (1,0) and pos[0] == bounds[0]-1:
        return (1, pos[1])
    if dir == (0,-1) and pos[1] == 1:
        return (pos[0], bounds[1] - 1)
    if dir == (0,1) and pos[1] == bounds[1]-1:
        return (pos[0], 1)
    
    return vadd(dir, pos)


def sim(m, bounds):
    n = defaultdict(list)
    for coord, blizzards in m.items():
        if blizzards == None:
            n[coord] = None
        else:
            for b in blizzards:
                n[next_blizzard(m, bounds, coord, b)].append(b)
    return n
        

def moves(m, pos):
    r = []
    if m[pos] is not None and len(m[pos]) == 0:
        r.append(pos)
    for d in dirs.values():
        n = vadd(d, pos)
        if n[1] < 0: continue
        if m[n] is not None and len(m[n]) == 0:
            r.append(n)
    return r


def printmap(m, bounds):
    for y in range(bounds[1]+1):
        for x in range(bounds[0]+1):
            c = ''
            if m[(x,y)] == None:
                c = '#'
            elif len(m[(x,y)]) == 0:
                c = '.'
            elif len(m[(x,y)]) == 1:
                c = to_dirs[m[(x,y)][0]]
            else:
                c = str(len(m[(x,y)]))
            print(c, end='')
        print()


def solve(filename):
    m, bounds, start, end = parse_file(filename)
    states = set([start])
    time = 0
    goals = [end, start, end]
    while len(goals):
        m = sim(m, bounds)
        t = set()
        for s in states:
            t.update(moves(m, s))
        states = t
        time += 1
        if goals[0] in states:
            print(f'{filename}: reached {goals[0]} at {time}')
            g = goals.pop(0)
            states = set([g])
            
    print(f'{filename}: finished at {time}')


# solve('simple.txt')
# solve('example.txt')
solve('input.txt')
