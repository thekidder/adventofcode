import math
import operator

def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        monkies = lines.split('\n\n')
        r = []
        for monkey in monkies:
            lines = monkey.split('\n')
            r.append({
                'items': list(map(int, lines[1][18:].split(','))),
                'expr': lines[2][19:],
                'test': int(lines[3][21:]),
                'true_monkey': int(lines[4][29:]),
                'false_monkey': int(lines[5][29:]),
                'inspected': 0,
            })
        return r


def round(monkies, reduce_fn):
    for m in monkies:
        while len(m['items']) > 0:
            m['inspected'] += 1
            old = m['items'].pop(0)
            item = reduce_fn(eval(m['expr']))
            next = m['true_monkey'] if item % m['test'] == 0 else m['false_monkey']
            monkies[next]['items'].append(item)


def score(monkies):
    return math.prod(sorted(map(lambda x: x['inspected'], monkies))[-2:])


def part1(filename):
    input = parse_file(filename)
    for _ in range(20):
        round(input, lambda x: x // 3)
    print(f'P1 MONKEY BZNZ {filename}: {score(input)}')


def part2(filename):
    input = parse_file(filename)
    total_m = math.prod(map(lambda x: x['test'], input))
    for _ in range(10000):
        round(input, lambda x: x % total_m)
    print(f'P2 MONKEY BZNZ {filename}: {score(input)}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
