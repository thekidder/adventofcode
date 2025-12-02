def parse_file(filename):
    with open(filename, 'r') as f:
        ranges = f.read().split(',')
        r = []
        for range in ranges:
            first, last = map(int, range.split('-'))
            r.append((first, last))
        return r


def valid(input):
    input = str(input)
    l = len(input)
    # print(f'VALID {input} {l} {input[:l//2] != input[l//2:]}')
    return input[:l//2] != input[l//2:]


def valid2(input):
    input = str(input)
    l = len(input)
    for i in range(1, l // 2 + 1):
        r = l // i
        if r * i != l:
            continue
        if input[:i] * r == input:
            return False
    return True


def solution(filename):
    input = parse_file(filename)
    ans_p1 = 0
    ans_p2 = 0
    for f, l in input:
        for id in range(f, l+1):
            if not valid(id):
                ans_p1 += id
            if not valid2(id):
                ans_p2 += id

    print(f'{filename}: P1 {ans_p1}, P2 {ans_p2}')


solution('example.txt')
solution('input.txt')
