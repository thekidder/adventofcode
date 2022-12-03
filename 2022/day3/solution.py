def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    return lines


def priority(item):
    if item <= 'Z':
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1


def part1(filename):
    input = parse_file(filename)
    ans = 0
    for line in input:
        a_set = set(line[:len(line)//2])
        b_set = set(line[len(line)//2:])
        for item in a_set:
            if item in b_set:
                ans += priority(item)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    ans = 0
    while len(input) > 0:
        group = input[:3]
        a_set = set(group[0])
        b_set = set(group[1])
        c_set = set(group[2])

        for item in a_set:
            if item in b_set and item in c_set:
                ans += priority(item)
                break

        input = input[3:]
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')
part2('example.txt')
part2('input.txt')
