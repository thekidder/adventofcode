import re

pattern = re.compile('(\w+)-to-(\w+) map:')

def parse_file(filename):
    maps = {}
    with open(filename, 'r') as f:
        lines = f.read()
        sections = lines.split('\n\n')
        seeds = sections[0]
        _, seeds = seeds.split(':')
        seeds = list(map(int, seeds.split()))
        sections = sections[1:]
        for section in sections:
            lines = section.split('\n')
            m = pattern.match(lines[0])
            fromtype = m.group(1)
            totype = m.group(2)

            ranges = lines[1:]
            ranges = list(map(lambda r: tuple(map(int, r.split())), ranges))
            maps[(fromtype, totype)] = ranges

        return seeds, maps


def transform(val, type, maps):
    for key, ranges in maps.items():
        if key[0] == type:
            for range in ranges:
                if val >= range[1] and val < range[1] + range[2]:
                    ind = val - range[1]
                    return range[0] + ind, key[1]
            return val, key[1]


def part1(filename):
    vals, maps = parse_file(filename)
    type = 'seed'
    while type != 'location':
        nexttype = type
        for i in range(len(vals)):
            vals[i], nexttype = transform(vals[i], type, maps)
        type = nexttype
    
    vals.sort()
    print(f'P1 {filename}: {vals[0]}')


def is_contained(src, dst):
    return src[0] >= dst[1] and src[0] + src[1] <= dst[1] + dst[2]


def is_distinct(src, dst):
    return src[0] >= dst[1] + dst[2] or src[0] + src[1] <= dst[1]


def transform_range(src_range, type, maps):
    for key, dst_ranges in maps.items():
        if key[0] == type:
            unmapped = [src_range]
            result_ranges = []
            for dst_range in dst_ranges:
                next_unmapped = []
                for src_range in unmapped:
                    if not is_distinct(src_range, dst_range):
                        l = src_range[1]
                        if src_range[0] < dst_range[1]:
                            next_unmapped.append((src_range[0], dst_range[1] - src_range[0]))
                            l -= dst_range[1] - src_range[0]

                        start = max(src_range[0], dst_range[1])
                        end = min(src_range[0] + src_range[1], dst_range[1] + dst_range[2])
                        ind = start - dst_range[1]
                        result_ranges.append((dst_range[0] + ind, end - start))
                        l -= (end - start)

                        if src_range[0] + src_range[1] > dst_range[1] + dst_range[2]:
                            next_unmapped.append((dst_range[1] + dst_range[2], l))
                        break
                    else:
                        next_unmapped.append(src_range)
                unmapped = next_unmapped
            return list(set(result_ranges + unmapped)), key[1]


def part2(filename):
    seed_indexes, maps = parse_file(filename)
    val_ranges = []
    for i in range(0, len(seed_indexes), 2):
        val_ranges.append((seed_indexes[i], seed_indexes[i+1]))

    type = 'seed'
    while type != 'location':
        next_ranges = []
        for pr in val_ranges:
            r, nexttype = transform_range(pr, type, maps)
            next_ranges.extend(r)
        val_ranges = next_ranges
        type = nexttype
    
    minloc = float('inf')
    for r in val_ranges:
        minloc = min(r[0], minloc)
    print(f'P2 {filename}: {minloc}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
