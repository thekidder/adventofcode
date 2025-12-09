import itertools
from helpers import *

def parse_file(filename):
    with open(filename, 'r') as f:
        return mapl(lambda x: tuple(map(int, x.split(','))), f.read().split('\n'))


def solve(filename, iterations=10):
    input = parse_file(filename)
    sorted_pairs = sorted([(sqr_dist(a, b), a, b) for a, b in itertools.combinations(input, 2)])

    circuits = {}
    deduped_circuits = {}
    for coord in input:
        circuits[coord] = set([coord])
        deduped_circuits[coord] = circuits[coord]

    for i in range(iterations):
        _, a, b = sorted_pairs[i]
        circuits[min(a,b)] |= circuits[max(a,b)]
        updated_circuit = circuits[min(a,b)]
        for circuit in updated_circuit:
            circuits[circuit] = updated_circuit
            if circuit == min(a,b):
                deduped_circuits[circuit] = updated_circuit
            elif circuit in deduped_circuits:
                del deduped_circuits[circuit]
            if len(deduped_circuits) == 1 and len(next(iter(deduped_circuits.values()))) == len(input):
                ans = a[0] * b[0]
                print(f'P2 {filename} ({iterations}): {ans}')
                return

    circuits_by_size = mapl(lambda x: (len(x), x), deduped_circuits.values())
    circuits_by_size.sort()
    ans = circuits_by_size[-1][0] * circuits_by_size[-2][0] * circuits_by_size[-3][0]
    print(f'P1 {filename} ({iterations}): {ans}')


solve('example.txt', 10)
solve('input.txt', 1000) 

solve('example.txt', 9999999999999999999)
solve('input.txt', 9999999999999999999)
