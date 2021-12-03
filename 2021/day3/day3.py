import collections

def part1(file):
    with open(file, 'r') as f:
        num_zeros = collections.defaultdict(int)
        num_ones = collections.defaultdict(int)
        for row in f:
            num = row.strip()
            for idx, bit in enumerate(num):
                if bit == '1':
                    num_ones[idx] += 1
                elif bit == '0':
                    num_zeros[idx] += 1
                else:
                    print('ERROR')
        idx = 0
        gamma_as_str = ''
        epsilon_as_str = ''
        while True:
            if idx in num_zeros and idx in num_ones:
                if num_ones[idx] > num_zeros[idx]:
                    gamma_as_str += '1'
                    epsilon_as_str += '0'
                else:
                    gamma_as_str += '0'
                    epsilon_as_str += '1'
            else:
                break
            idx+=1
        print(f'got gamma {int(gamma_as_str, 2)} and epsilon {int(epsilon_as_str, 2)}')
        print(f'answer: {int(gamma_as_str, 2)*int(epsilon_as_str, 2)}')


def most_common(nums, idx):
    num_zeros = 0
    num_ones = 0
    for num in nums:
        if num[idx] == '1':
            num_ones += 1
        elif num[idx] == '0':
            num_zeros += 1
        else:
            print('ERROR')
    if num_zeros > num_ones:
        return '0'
    else:
        return '1'


def part2(file):
    with open(file, 'r') as f:
        nums = []
        for row in f:
            num = row.strip()
            nums.append(num)
    
    ox = nums[:]
    idx = 0
    while len(ox) > 1:
        mvp = most_common(ox, idx)
        ox = [n for n in filter(lambda n: n[idx] == mvp, ox)]
        print(f'{mvp} {idx} {len(ox)}')
        idx += 1

    co2 = nums[:]
    idx = 0
    while len(co2) > 1:
        mvp = most_common(co2, idx)
        co2 = [n for n in filter(lambda n: n[idx] != mvp, co2)]
        print(f'{mvp} {idx} {len(co2)}')
        idx += 1

    print(f'got oxygen {int(ox[0], 2)}, co2 {int(co2[0], 2)} total {int(ox[0], 2)*int(co2[0], 2)}')




part2('input.txt')