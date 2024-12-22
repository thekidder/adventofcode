from collections import defaultdict
def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(int(line))

    return lines


def mix(secret, val):
    return secret ^ val


def prune(secret):
    return secret % 16777216


def next(secret):
    r = prune(mix(secret, 64 * secret))
    r = prune(mix(r, r // 32))
    return prune(mix(r, 2048 * r))


def part1(filename):
    input = parse_file(filename)
    for _ in range(2000):
        for i, s in enumerate(input):
            input[i] = next(s)

    ans = sum(input)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)

    changes = [[]]*len(input)
    profits = []
    for _ in input:
        profits.append(defaultdict(int))
    for iter in range(2000):
        if iter % 100 == 0:
            print(f'iter {iter}/2000')
        for i,s in enumerate(input):
            l = s
            input[i] = next(s)
            p = input[i] % 10
            c = p - (l%10)
            changes[i] = changes[i] + [c]
            changes[i] = changes[i][-4:]
            if len(changes[i]) == 4:
                key = tuple(changes[i])
                if key not in profits[i]:
                    profits[i][key] = p

    all_seqs = set()
    for p in profits:
        all_seqs.update(p.keys())
    max_profit = 0
    for seq in all_seqs:
        profit = 0
        for p in profits:
            profit += p[seq]
        max_profit = max(profit, max_profit)

    print(f'P2 {filename}: {max_profit}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
