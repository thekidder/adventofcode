import itertools

def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        return lines.split('\n')


def part1(filename):
    input = parse_file(filename)
    ans = 0

    for bank in input:
        r = 0
        for x in itertools.combinations(bank, 2):
            r = max(r, int(''.join(x)))
        ans += r

    print(f'P1 {filename}: {ans}')


def build_joltage(acc, bank, digits):
    if digits == 0:
        return acc
    if len(bank) < digits:
        print('ERROR')
        return acc # TODO
    
    for digit in range(9, 0, -1):
        for i, x in enumerate(bank):
            if int(x) == digit and len(bank) - 1 - i >= digits - 1:
                return build_joltage(acc + x, bank[i+1:], digits - 1)


def part2(filename):
    input = parse_file(filename)
    ans = 0

    for bank in input:
        r = int(build_joltage('', bank, 12))
        ans += r

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
