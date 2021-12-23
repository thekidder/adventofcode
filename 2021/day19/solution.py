import itertools

import re

scanner = re.compile('--- scanner (\d+) ---')
pos = re.compile('(-?\d+),(-?\d+),(-?\d+)')

def parse_file(filename):
    scanners = []
    with open(filename, 'r') as f:
        for line in f:
            m = scanner.match(line)
            if m is not None:
                scanners.append([])
            else:
                m = pos.match(line)
                if m is not None:
                    scanners[-1].append((int(m.group(1)),int(m.group(2)),int(m.group(3))))

    return scanners


def relative_to(pos, anchor):
    return (pos[0]-anchor[0],pos[1]-anchor[1],pos[2]-anchor[2])


#(sign, index) for each of three dimensions x 24 orientations
rotations = [((1, 1), (1, 0), (-1, 2)), ((-1, 1), (1, 2), (-1, 0)), ((1, 2), (1, 1), (-1, 0)), ((1, 2), (1, 0), (1, 1)), ((-1, 2), (1, 0), (-1, 1)), ((-1, 1), (1, 0), (1, 2)), ((1, 0), (-1, 2), (1, 1)), ((1, 0), (-1, 1), (-1, 2)), ((-1, 2), (-1, 0), (1, 1)), ((1, 1), (-1, 0), (1, 2)), ((1, 2), (-1, 0), (-1, 1)), ((1, 1), (-1, 2), (-1, 0)), ((-1, 1), (-1, 0), (-1, 2)), ((-1, 0), (-1, 1), (1, 2)), ((-1, 2), (-1, 1), (-1, 0)), ((-1, 0), (1, 2), (1, 1)), ((-1, 0), (-1, 2), (-1, 1)), ((1, 0), (1, 1), (1, 2)), ((1, 0), (1, 2), (-1, 1)), ((-1, 0), (1, 1), (-1, 2)), ((1, 2), (-1, 1), (1, 0)), ((1, 1), (1, 2), (1, 0)), ((-1, 1), (-1, 2), (1, 0)), ((-1, 2), (1, 1), (1, 0))]

def orientations():
    for o in rotations:
        yield lambda pos: (o[0][0] * pos[o[0][1]], o[1][0] * pos[o[1][1]], o[2][0] * pos[o[2][1]])
    

def matches(fingerprint, beacons, anchor_index):
    f2 = set()
    anchor = beacons[anchor_index]
    for beacon in beacons:
        b = relative_to(beacon, anchor)
        f2.add(b)

    intersection = f2 & fingerprint
    return len(intersection) >= 12


def find_match(ground_truth, input, scanner_pos):
    for i, scanner in enumerate(input):
        for orientation in orientations():
            transformed_beacons = [orientation(b) for b in scanner]
            for ground in ground_truth:
                for anchor in ground[:-11]:
                    negative_anchor = (-anchor[0], -anchor[1], -anchor[2])
                    fingerprint = set([relative_to(b, anchor) for b in ground])

                    for a in range(len(transformed_beacons)-11):
                        other_anchor = transformed_beacons[a]
                        if matches(fingerprint, transformed_beacons, a):
                            spos = (-(negative_anchor[0]+other_anchor[0]), -(negative_anchor[1]+other_anchor[1]), -(negative_anchor[2]+other_anchor[2]))
                            scanner_pos.append(spos)
                            g = [relative_to(relative_to(b, other_anchor), negative_anchor) for b in transformed_beacons]
                            # print(f'NEW GROUND: {g}')
                            ground_truth.append(g)

                            del input[i]
                            return


def solve(filename):
    input = parse_file(filename)

    ground_truth = [input[0]]
    scanner_pos = [(0,0,0)]
    input = input[1:]

    while len(input) > 0:
        find_match(ground_truth, input, scanner_pos)

    dist = 0
    for i,j in itertools.combinations(range(len(scanner_pos)),2):
        l = scanner_pos[i]
        r = scanner_pos[j]
        d = abs(l[0] - r[0]) + abs(l[1] - r[1]) + abs(l[2] - r[2])
        dist = max(d, dist)

    all_beacons = set()
    for scanner in ground_truth:
        all_beacons |= set(scanner)
    print(f'num beacons: {len(all_beacons)}, max distance: {dist}')
    all_beacons = sorted(all_beacons)


solve('input.txt')
