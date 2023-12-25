from collections import defaultdict
import math
import networkx as nx 
import matplotlib.pyplot as plt 


def parse_file(filename):
    lines = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            name, cnt = line.split(':')
            cnt = cnt.split()

            lines[name].extend(cnt)
            for n in cnt:
                lines[n].append(name)

    return lines


def exists_in(groups, graph, cmpt):
    idxes = []
    for i, g in enumerate(groups):
        if cmpt in g:
            idxes.append(i)
        for h in graph[cmpt]:
            if h in g and i not in idxes:
                idxes.append(i)
    return idxes


def ngroups(graph):
    groups = []
    for g in graph.keys():
        idxes = exists_in(groups, graph, g)
        if len(idxes) == 0:
            groups.append(set([g]))
            idx = -1
        elif len(idxes) == 1:
            groups[idxes[0]].add(g)
            idx = idxes[0]
        else:
            s = groups.pop(idxes[1])
            groups[idxes[0]] |= s
            idx = idxes[0]
            
        for h in graph[g]:
            groups[idx].add(h)
    return len(groups), math.prod(map(len, groups))
        

def disconnect(input, a, b):
    input[a].remove(b)
    input[b].remove(a)


def part1(filename):
    input = parse_file(filename)

    visual = []
    for g,cnt in input.items():
        for h in cnt:
            visual.append([g,h])

    G = nx.Graph() 
    G.add_edges_from(visual) 
    nx.draw_networkx(G) 
    plt.show() 

    disconnect(input, 'mtq', 'jtr')
    disconnect(input, 'ddj', 'znv')
    disconnect(input, 'pzq','rrz')

    n, ans = ngroups(input)
    print(f'P1 {filename}: {ans}')


part1('example.txt')
# part1('input.txt')
