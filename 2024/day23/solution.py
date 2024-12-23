from collections import defaultdict
import itertools

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(tuple(map(lambda x: x.strip(), line.split('-'))))

    return lines


def part1(filename):
    input = parse_file(filename)
    all_connections = defaultdict(set)
    pcs = set()
    for a, b in input:
        all_connections[a].add(b)
        all_connections[b].add(a)
        pcs.update([a,b])

    lans = set()
    for c in pcs:
        if c[0] != 't':
            continue
        for a,b in itertools.combinations(all_connections[c], 2):
            if b in all_connections[a]:
                lans.add(tuple(sorted([a,b,c])))                   

    print(f'P1 {filename}: {len(lans)}')


def connected(all_connections, pcs):
    # print(f'connected {pcs}')
    for a,b in itertools.combinations(pcs, 2):
        # print(f'{a}, {b}')
        if b not in all_connections[a]:
            return False
    return True


def part2(filename):
    input = parse_file(filename)

    all_connections = defaultdict(set)
    lans = []
    for a, b in input:
        all_connections[a].add(b)
        all_connections[b].add(a)
        lans.append(set([a,b]))

    for a, b in input:
        for lan in lans:
            combined = set([a,b]) | lan
            if combined == lan:
                continue
            if connected(all_connections, combined):
                lan.update([a,b])

    m = 0
    for lan in lans:
        if len(lan) > m:
            m = len(lan)
            ans = lan

    ans = ','.join(sorted(ans))

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
