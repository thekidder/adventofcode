import copy
import heapq
import re

pattern = re.compile('Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.*)')

def parse_file(filename):
    tunnels = {}
    flows = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            m = pattern.match(line)
            src = m.group(1)
            flow = int(m.group(2))
            dsts = list(map(lambda x: x.strip(), m.group(3).split(',')))
            flows[src] = flow
            tunnels[src] = dsts

        return tunnels, flows


def est_max_total(time, closed_valves, flows, p):
    total = 0
    closed_valves = sorted(list(closed_valves), key=lambda x: flows[x], reverse=True)
    while len(closed_valves):
        time -= 2
        for _ in range(p):
            if len(closed_valves) == 0:
                continue
            v = closed_valves.pop(0)
            if time <= 0:
                break
            total += time * flows[v]
    return total


def build_costs(tunnels):
    routes = {}

    for a in tunnels.keys():
        for b in tunnels[a]:
            n = tuple(sorted([a,b]))
            routes[n] = 1

    done = False
    while not done:
        done = True
        keys = list(routes.keys())
        for i in range(len(routes)):
            r = keys[i]
            cost = routes[r]
            a, b = r
            for c in tunnels[b]:
                n = tuple(sorted([a,c]))
                if a != c and (n not in routes or cost + 1 < routes[n]):
                    routes[n] = cost + 1
                    done = False
            for d in tunnels[a]:
                n = tuple(sorted([b,d]))
                if b != d and (n not in routes or cost + 1 < routes[n]):
                    routes[n] = cost + 1
                    done = False
    return routes


def part1(filename):
    tunnels, flows = parse_file(filename)
    routes = build_costs(tunnels)

    non_zero_flow = set(filter(lambda x: flows[x]>0, tunnels.keys()))

    paths = [
        {
            'time': 30,
            'total': 0,
            'closed': non_zero_flow,
            'loc': 'AA',
            'route': [],
            'max_est': est_max_total(30, non_zero_flow, flows)
        }
    ]
    max_flow = 0
    while len(paths) > 0:
        p = paths.pop()

        if p['max_est'] < max_flow or p['time'] <= 0:
            continue

        for loc in tunnels.keys():
            if loc not in p['closed']: 
                continue
            move_cost = routes[tuple(sorted([loc, p['loc']]))]
            t = p['time'] - 1 - move_cost
            total = p['total'] + t * flows[loc]
            closed = p['closed'] - set([loc])
            next_p = {
                'time': t,
                'total': total,
                'closed': closed,
                'loc': loc,
                'max_est': total + est_max_total(t, closed, flows),
                'route': p['route'] + [loc]
            }
            paths.append(next_p)
            max_flow = max(max_flow, total)

    print(f'P1 {filename}: {max_flow}')


def actions(p, entity, tunnels, flows, routes):
    if p[entity]['next_action'] > 0:
        return
    loc = p[entity]['loc']
    if loc in p['closed']:
        next_p = copy.deepcopy(p)
        next_p[entity]['next_action'] = 1
        next_p['closed'].remove(loc)
        next_p['total'] += next_p['time'] * flows[loc]
        next_p['max_est'] = next_p['total'] + est_max_total(next_p['time'], next_p['closed'], flows, 2)
        yield next_p
    else:
        closed = sorted(p['closed'], key = lambda x: flows[x], reverse=True)
        for next_loc in closed:
            next_p = copy.deepcopy(p)
            next_p[entity]['next_action'] = routes[tuple(sorted([loc, next_loc]))]
            next_p[entity]['loc'] = next_loc
            next_p[entity]['route'].append(next_loc)
            yield next_p


def part2(filename):
    tunnels, flows = parse_file(filename)
    routes = build_costs(tunnels)

    non_zero_flow = set(filter(lambda x: flows[x]>0, tunnels.keys()))

    paths = [
        (0, 0, {
            'time': 26,
            'total': 0,
            'closed': non_zero_flow,
            'me': {
                'loc': 'AA',
                'next_action': 1,
                'route': [],
            },
            'elephant': {
                'loc': 'AA',
                'next_action': 1,
                'route': [],
            },
            'max_est': est_max_total(26, non_zero_flow, flows, 2)
        })
    ]
    print(paths)
    max_flow = 0
    i = 0
    while len(paths) > 0:
        _, _, p = heapq.heappop(paths)

        p['time'] -= 1
        p['me']['next_action'] -= 1
        p['elephant']['next_action'] -= 1

        if p['me']['next_action'] > 0 and p['elephant']['next_action'] > 0:
            i += 1
            heapq.heappush(paths, (-p['total'], i, p))
            continue

        if p['max_est'] < max_flow or p['time'] <= 0 or len(p['closed']) == 0:
            continue
        
        next = []
        me_actions = list(actions(p, 'me', tunnels, flows, routes))
        if len(me_actions) == 0:
            next = list(actions(p, 'elephant', tunnels, flows, routes))
        else:
            for me_p in me_actions:
                elephant_actions = list(actions(me_p, 'elephant', tunnels, flows, routes))
                if len(elephant_actions) == 0:
                    next = me_actions
                else:
                    for action in elephant_actions:
                        if action['me']['loc'] != action['elephant']['loc']:
                            next.append(action)

        for p in next:
            i += 1
            if p['max_est'] > max_flow:
                heapq.heappush(paths, (-p['total'], i, p))
            if p['total'] > max_flow:
                print(f'FOUND NEW MAX {p["total"]} {p}')
            max_flow = max(max_flow, p['total'])
    print(f'P2 {filename}: {max_flow}')


# part1('example.txt')
# part1('input.txt')

# part2('example.txt')
part2('input.txt')
