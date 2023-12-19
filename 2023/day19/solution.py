import re

pattern = re.compile('(\w+)\{(.*)\}$')
partp = re.compile('\{(.*)\}$')

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.read()
        workflows,parts = lines.split('\n\n')
        workflows = workflows.split()
        ww = {}
        for w in workflows:
            rr = []
            m = pattern.match(w)
            name = m.group(1)
            rules = m.group(2).split(',')
            for r in rules:
                if ':' in r:
                    r1, r2 = r.split(':')
                    rr.append((r1[0], r1[1], int(r1[2:]), r2))
                else:
                    rr.append((r,))
            ww[name] = rr

        pp = []
        parts = parts.split()
        for p in parts:
            partdesc = {}
            x = partp.match(p).group(1).split(',')
            for var in x:
                partdesc[var[0]] = int(var[2:])
            pp.append(partdesc)

        return ww,pp


def apply(workflow, part):
    for rule in workflow:
        if len(rule) == 1:
            return rule[0]
        var = rule[0]
        if rule[1] == '<' and part[var] < rule[2]:
            return rule[3]
        elif rule[1] == '>' and part[var] > rule[2]:
            return rule[3]


def part1(filename):
    workflows,parts = parse_file(filename)
    ans = 0
    for part in parts:
        workflow = 'in'
        while workflow != 'A' and workflow != 'R':
            workflow = apply(workflows[workflow], part)
        if workflow == 'A':
            ans += part['x'] + part['m'] + part['a'] + part['s']

    print(f'P1 {filename}: {ans}')


def split_state(var_ranges, rule):
    var = rule[0]
    range = var_ranges[var]
    if rule[1] == '<':
        if range[0] >= rule[2]:
            return None, var_ranges
        if range[1] < rule[2]:
            return var_ranges, None
        pass_range = dict(var_ranges)
        pass_range[var] = (var_ranges[var][0],rule[2]-1)
        fail_range = dict(var_ranges) 
        fail_range[var] = (rule[2],var_ranges[var][1])
        return pass_range,fail_range
    else:
        if range[1] <= rule[2]:
            return None, var_ranges
        if range[0] > rule[2]:
            return var_ranges, None
        pass_range = dict(var_ranges)
        pass_range[var] = (rule[2]+1,var_ranges[var][1])
        fail_range = dict(var_ranges) 
        fail_range[var] = (var_ranges[var][0],rule[2])
        return pass_range,fail_range


def part2(filename):
    workflows,_ = parse_file(filename)
    val_min = 1
    val_max = 4000
    ans = 0

    # workflow, rule index, state with val ranges
    states = [('in',0,{'x':(val_min,val_max),'m':(val_min,val_max),'a':(val_min,val_max),'s':(val_min,val_max)})]

    accepted = []

    while len(states) > 0:
        state = states.pop()
        if state[0] == 'A':
            accepted.append(state[2])
            continue
        elif state[0] == 'R':
            continue

        workflow = workflows[state[0]]
        rule = workflow[state[1]]

        if len(rule) == 1:
            states.append((rule[0],0,state[2]))
        else:
            pass_state,fail_state = split_state(state[2], rule)
            if pass_state is not None:
                states.append((rule[3],0,pass_state))
            if fail_state is not None:
                states.append((state[0],state[1]+1,fail_state))

    for a in accepted:
        ans += (a['x'][1] - a['x'][0] + 1) * \
            (a['m'][1] - a['m'][0] + 1) * \
            (a['a'][1] - a['a'][0] + 1) * \
            (a['s'][1] - a['s'][0] + 1)

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')
