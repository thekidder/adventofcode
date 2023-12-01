def part1(filename):
    ans = 0
    with open(filename, 'r') as f:
        for l in f:
            nums = [x for x in l if x >= '0' and x <= '9']
            ans += int(nums[0] + nums[-1])
    print(f'P1 {filename}: {ans}')

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def part2(filename):
    ans = 0
    with open(filename, 'r') as f:
        for l in f:
            l = l.replace('one', 'o1e')
            l = l.replace('two', 't2o')
            l = l.replace('three', 't3e')
            l = l.replace('four', 'f4r')
            l = l.replace('five', 'f5e')
            l = l.replace('six', 's6x')
            l = l.replace('seven', 's7n')
            l = l.replace('eight', 'e8t')
            l = l.replace('nine', 'n9e')
            nums = [x for x in l if x >= '0' and x <= '9']
            ans += int(nums[0] + nums[-1])
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
