from collections import defaultdict


def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            hand, bid = line.split()
            lines.append((hand.strip(), int(bid)))

    return lines


val = {
    'A': 12, 
    'K': 11, 
    'Q': 10, 
    'J': 9, 
    'T': 8, 
    '9': 7, 
    '8': 6, 
    '7': 5, 
    '6': 4, 
    '5': 3, 
    '4': 2, 
    '3': 1,
    '2': 0
}

val_j = {
    'A': 12, 
    'K': 11, 
    'Q': 10, 
    'T': 9, 
    '9': 8, 
    '8': 7, 
    '7': 6, 
    '6': 5, 
    '5': 4, 
    '4': 3, 
    '3': 2,
    '2': 1,
    'J': 0 
}


def ords(hand, wildj = False):
    cnt = defaultdict(int)
    jcnt = 0
    for c in hand:
        if not wildj or c != 'J':
            cnt[c] += 1
        elif wildj:
            jcnt += 1
    return sorted(cnt.values(), reverse = True), jcnt


def has(hand, n, m = None, wildj = False):
    cnt, jcnt = ords(hand, wildj = wildj)
    if len(cnt) == 0 and wildj:
        return jcnt == n
    if wildj:
        cnt[0] += jcnt
    if m is None:
        return cnt[0] == n
    return cnt[0] == n and cnt[1] == m


def hand_key(hand, wildj):
    v = 0
    hand = hand[0]
    if wildj:
        vals = val_j
    else:
        vals = val
    for i, c in enumerate(reversed(hand)):
        v += vals[c] * 13**(i)

    if has(hand, 5, wildj=wildj):
        v += 6*500000
    elif has(hand, 4, wildj=wildj):
        v += 5*500000
    elif has(hand, 3, 2, wildj=wildj):
        v += 4*500000
    elif has(hand, 3, wildj=wildj):
        v += 3*500000
    elif has(hand, 2, 2, wildj=wildj):
        v += 2*500000
    elif has(hand, 2, wildj=wildj):
        v += 500000

    return v


def part1(filename):
    input = parse_file(filename)
    input = sorted(input, key = lambda h: hand_key(h, False))
    ans = 0
    for i, h in enumerate(input):
        ans += (i+1) * h[1]
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    input = sorted(input, key = lambda h: hand_key(h, True))
    ans = 0
    for i, h in enumerate(input):
        ans += (i+1) * h[1]
    print(f'P1 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
