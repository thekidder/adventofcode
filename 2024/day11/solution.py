from collections import defaultdict

def parse_file(filename):
    with open(filename, 'r') as f:
        return list(map(int, f.read().split()))


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


def solve(filename, i):
    input = parse_file(filename)
    nums = defaultdict(int)

    for n in input:
        nums[n] += 1
    
    for _ in range(i):
        nums = blink_dict(nums)

    ans = sum(nums.values())

    print(f'{filename} after {i} iterations: {ans}')


solve('example.txt', 25)
solve('input.txt', 25)

solve('example.txt', 75)
solve('input.txt', 75)
