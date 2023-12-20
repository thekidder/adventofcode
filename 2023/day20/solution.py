from collections import defaultdict

def parse_file(filename):
    lines = {}
    with open(filename, 'r') as f:
        inputs = defaultdict(list)
        for line in f:
            name, recv = line.split('->')
            name = name.strip()
            type = 'b'
            recv = list(map(lambda s: s.strip(), recv.strip().split(',')))
            data = None
            if name[0] == '%':
                type = '%'
                name = name[1:]
                data = 0
            if name[0] == '&':
                type = '&'
                name = name[1:]
            for r in recv:
                inputs[r].append(name)
            lines[name] = (type, recv, data, None)

    for name,data in lines.items():
        lines[name] = (data[0], data[1], data[2], dict(map(lambda r: (r, 0), inputs[name])))

    return lines


def get_state(input):
    states = []
    for n in sorted(input.keys()):
        if input[n][2] is None and input[n][3] is None:
            continue
        states.append(n)
        if input[n][2] is not None:
            states.append(input[n][2])
        else:
            dd = []
            for m in sorted(input[n][3].keys()):
                dd.append(input[n][3][m])
            states.append(tuple(dd))
    # print('global state', tuple(states))

    return tuple(states)


def part1(filename):
    input = parse_file(filename)
    # print(input)
    cntl = 0
    cnth = 0

    # get_state(input)
    # last_seen = {get_state(input): 0}

    first_on = {}

    i = 0

    sends_high = {
        'bt': None, 'dl': None, 'fr': None, 'rv': None,
    }

    while not all(sends_high.values()):
    # while i < 10000:
        i += 1
        pulses = [('button', 'broadcaster', 0)]
        while len(pulses) > 0:
            sender,recv,pulse = pulses.pop(0)
            if pulse == 0:
                cntl += 1
            else:
                cnth += 1
            if sender in sends_high and recv == 'rs' and pulse == 1:
                print(f'{pulse} to {recv} from {sender} at {i}')
                sends_high[sender] = i
            if recv not in input:
                continue 
            type = input[recv][0]
            if type == 'b':
                # print(f'{sender} -{pulse}> {recv} (bcast)')
                for r in input[recv][1]:
                    pulses.append((recv, r, pulse))
            elif type == '%':
                # print(f'{sender} -{pulse}> {recv} (flip)')
                if pulse == 0:
                    state = input[recv][2]
                    input[recv] = (input[recv][0], input[recv][1], 0 if state else 1, input[recv][3])
                    p = 0 if state else 1
                    for r in input[recv][1]:
                        pulses.append((recv, r, p))
            else:
                # print(f'{sender} -{pulse}> {recv} (conj)')
                input[recv][3][sender] = pulse
                # print(input[recv][2])
                if all(input[recv][3].values()):
                    p = 0
                else:
                    p = 1
                for r in input[recv][1]:
                    pulses.append((recv, r, p))

        # s = get_state(input)
        # if s in last_seen:
        #     print(i, s)
        #     break
        # last_seen[s] = i
        # for n,d in input.items():
        #     if n == 'broadcaster':
        #         continue
        #     if n in first_on:
        #         continue
        #     if d[0] == '%':
        #         is_on = d[2] 
        #     else:
        #         is_on = all(tuple(map(lambda x: d[3][x], sorted(d[3].keys()))))
        #     if is_on:
        #         first_on[n] = i
        # not_seen = set(input.keys()) - set(first_on.keys() - ['broadcaster'])
        # print(not_seen)

        # print(first_on)
    print(sends_high)
    print(f'P1 {filename}: {cntl*cnth} ({cntl}, {cnth})')


def part2(filename):
    input = parse_file(filename)
    print(input)
    seen = set()
    deps = [('rx', 0)]
    while len(deps) > 0:
        dep,needed_pulse = deps.pop(0)
        if dep in input:
            print(f'{dep} is of type {input[dep][0]}')
        seen.add(dep)
        for n,d in input.items():
            if dep in d[1]:
                print(f'{n} feeds {dep}')
                if d[0] == '%':
                    print(f'{n} needs a low-pulse from any of {d[3].keys()} and to be equal to {0 if needed_pulse else 1}')
                    for k in d[3].keys():
                        if k not in seen:
                            deps.append((k,0))
                elif d[0] == '&':
                    if needed_pulse == 1:
                        print(f'{n} needs a low-pulse from any of {d[3].keys()}')
                    else:
                        print(f'{n} needs a high-pulse from all of {d[3].keys()}')
                    for k in d[3].keys():
                        if k not in seen:
                            deps.append((k, 0 if needed_pulse == 1 else 1))
                



    # # ans = 0
    # print(f'P2 {filename}: {ans}')


# part1('example2.txt')
part1('input.txt')

# part2('example.txt')
# not 618970019642690137449562112
# part2('input.txt')
