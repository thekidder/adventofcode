def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            levels = list(map(int, line.split()))
            lines.append(levels)

    return lines


def safe(levels):
    if levels[1] < levels[0]:
        levels = list(reversed(levels))
    
    last = 0
    for v in levels:
        if last == 0:
            last = v
            continue

        if v <= last:
            return False
        if v - last >3:
            return False

        last = v
    return True


def part1(filename):
    input = parse_file(filename)
    ans = sum([1 if safe(x) else 0 for x in input])
    print(f'P1 {filename}: {ans}')


def safe_ext(levels):
    if safe(levels):
        return True
    else:
        for i in range(len(levels)):
            l = levels[:]
            del l[i]
            if safe(l):
                return True
    return False


def part2(filename):
    input = parse_file(filename)
    ans = sum([1 if safe_ext(x) else 0 for x in input])
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
