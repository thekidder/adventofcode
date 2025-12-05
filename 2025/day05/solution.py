def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.read()
        r = []
        ranges, ingredients = lines.split('\n\n')
        for range in ranges.split('\n'):
            fi, l = range.split('-')
            r.append((int(fi), int(l)))
        i = list(map(int, ingredients.split('\n')))

        return r, i


def part1(filename):
    ranges, ingredients = parse_file(filename)
    ans = 0

    for i in ingredients:
        for r in ranges:
            if i >= r[0] and i <= r[1]:
                ans += 1
                break

    print(f'P1 {filename}: {ans}')


def part2(filename):
    ranges, _ = parse_file(filename)
    ans = 0

    ranges = sorted(ranges, key = lambda r: r[0])

    output = []

    last = ranges[0]
    for r in ranges[1:]:
        if r[0] <= last[1]:
            last = (last[0], max(r[1], last[1]))
        else:
            output.append(last)
            last = r
    
    if last != ranges[-1]:
        output.append(last)

    for r in output:
        ans += r[1] - r[0] + 1

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
