from collections import defaultdict

def parse_file(filename):
    with open(filename, 'r') as f:
        return list(map(int, f.read().split()))


def blink(x):
    r = []
    for v in x:
        if v == 0:
            r.append(1)
        elif len(str(v)) % 2 == 0:
            as_str = str(v)
            r.append(int(as_str[:len(as_str)//2]))
            r.append(int(as_str[len(as_str)//2:]))
        else:
            r.append(2024*v)
    return r


def blink_dict(x):
    r = defaultdict(int)
    for k,v in x.items():
        if k == 0:
            r[1] += v
        elif len(str(k)) % 2 == 0:
            as_str = str(k)
            r[int(as_str[:len(as_str)//2])] += v
            r[int(as_str[len(as_str)//2:])] += v
        else:
            r[2024*k] += v
    return r


def part1(filename):
    input = parse_file(filename)

    for _ in range(25):
        input = blink(input)

    print(f'P1 {filename}: {len(input)}')


def part2(filename):
    input = parse_file(filename)
    nums = defaultdict(int)

    for n in input:
        nums[n] += 1
    
    for _ in range(75):
        nums = blink_dict(nums)

    ans = sum(nums.values())

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
