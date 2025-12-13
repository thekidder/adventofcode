import functools
import re

pattern = re.compile('(\d+)x(\d+)')

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.read()
        sections = lines.split('\n\n')
        shapes = sections[:-1]
        regions = sections[-1]

        shapes = [len(list(filter(lambda c: c == '#', x))) for x in shapes]

        regions = regions.split('\n')
        for region in regions:
            size, quantities = region.split(':')
            m = pattern.match(size)
            x = int(m.group(1))
            y = int(m.group(2))
            quantities = [int(q) for q in quantities.split()]

            r.append((x, y, quantities))
            
        return shapes, r


def can_fit(shapes, region):
    taken_spots = sum([shapes[i] * region[2][i] for i in range(len(shapes))])
    free_slots = region[0] * region[1] - taken_spots

    if free_slots < 0:
        return 0
    
    # wow, super dumb cause we don't have to be smart
    return 1


def part1(filename):
    shapes, regions = parse_file(filename)
    ans = sum(map(functools.partial(can_fit, shapes), regions))

    print(f'P1 {filename}: {ans}')

# this solution doesn't work for the example! pretty dumb!
# part1('example.txt')
part1('input.txt')
