from collections import Counter

def parse_file(filename):
    rules = {}
    with open(filename, 'r') as f:
        template = f.readline().strip()
        for line in f:
            if '->' in line:
                rule = line.split('->')
                rules[rule[0].strip()] = rule[1].strip()

    return template, rules


def pairs(template):
    for i in range(len(template) - 1):
        yield template[i:i+2]


def part1(filename):
    template,rules = parse_file(filename)
    print(rules)
    for i in range(10):
        out = ''
        for pair in pairs(template):
            out += pair[0]
            if pair in rules:
                out += rules[pair]
        out += template[-1]
        template = out

        print(f'ITERATION {i+1}: {out}')

    cnt = Counter(out)
    top = cnt.most_common()
    print(top[0][1] - top[-1][1])


def part2(filename):
    template,rules = parse_file(filename)
    polymer = Counter(pairs(template))

    for _ in range(40):
        next = Counter(polymer)

        for rule, cnt in polymer.items():
            new_letter = rules[rule]
            next[rule] -= cnt
            next[rule[0] + new_letter] += cnt
            next[new_letter + rule[1]] += cnt

        polymer = next

    cnts = Counter([template[0]])
    for rule, cnt in polymer.items():
        cnts[rule[1]] += cnt

    top = cnts.most_common()
    print(int(top[0][1] - top[-1][1]))


part2('input.txt')
