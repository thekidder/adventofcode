from functools import reduce

def mapl(fn, itr):
    return list(map(fn, itr))


def parse_file(filename):
    with open(filename, 'r') as f:
        ranges, ingredients = f.read().split('\n\n')
        return mapl(lambda r: mapl(int, r.split('-')), ranges.split('\n')), \
            mapl(int, ingredients.split('\n'))


def part1(filename):
    ranges, ingredients = parse_file(filename)

    def in_range(acc, i):
        for r in ranges:
            if i >= r[0] and i <= r[1]:
                return acc + 1
        return acc

    ans = reduce(in_range, ingredients, 0)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    ranges = sorted(parse_file(filename)[0], key = lambda r: r[0])

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

    ans = reduce(lambda acc, r: acc + r[1] - r[0] + 1, output, 0)
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
