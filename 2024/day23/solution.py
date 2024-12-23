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


def connected(edges, subgraph):
    for a,b in itertools.combinations(subgraph, 2):
        if b not in edges[a]:
            return False
    return True


def part2(filename):
    input = parse_file(filename)

    edges = defaultdict(set)
    lans = []
    for a, b in input:
        edges[a].add(b)
        edges[b].add(a)
        lans.append(set([a,b]))

    for a, b in input:
        for lan in lans:
            combined = set([a,b]) | lan
            if combined == lan:
                continue
            if connected(edges, combined):
                lan.update([a,b])

    ans = max(lans, key = lambda x: len(x))
    ans = ','.join(sorted(ans))

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
