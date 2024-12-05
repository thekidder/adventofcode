def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        r,p = lines.split('\n\n')

        rules = []
        for l in r.split('\n'):
            a,b = l.split('|')
            rules.append((int(a), int(b)))

        updates = []
        for l in p.split('\n'):
            update = []
            for u in l.split(','):
                update.append(int(u))
            updates.append(update)

        return rules,updates


def ordered(update, rules):
    for rule in rules:
        try:
            ia = update.index(rule[0])
            ib = update.index(rule[1])
            if ia > ib:
                return False
        except:
            pass
    return True



def part1(filename):
    rules,updates = parse_file(filename)

    ans = 0
    for update in updates:
        if ordered(update, rules):
            ans += update[len(update) // 2]

    print(f'P1 {filename}: {ans}')


def order(update, rules):
    while not ordered(update, rules):
        for rule in rules:
            try:
                ia = update.index(rule[0])
                ib = update.index(rule[1])
                if ia > ib:
                    update[ia] = rule[1]
                    update[ib] = rule[0]
            except:
                pass
    return update


def part2(filename):
    rules,updates = parse_file(filename)

    ans = 0
    for update in updates:
        if not ordered(update, rules):
            updated = order(update, rules)
            ans += updated[len(update) // 2]

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
