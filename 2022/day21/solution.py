import operator
import re

from helpers import *

pattern = re.compile('\d+')

def parse_file(filename):
    r = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip()
            monkey, expr = l.split(':')
            expr = expr.strip()
            m = pattern.match(expr)
            if m is not None:
                r[monkey] = [int(expr), [], set()]
            else:
                deps = [expr[:4], expr[-4:]]
                r[monkey] = [expr, deps, set(deps)]


        return r


def e(input, expr):
    m1 = input[expr[:4]][0]
    m2 = input[expr[-4:]][0]
    op = expr[5]

    if op == '*':
        return m1 * m2
    elif op == '+':
        return m1 + m2
    elif op == '-':
        return m1 - m2
    else:
        return m1 // m2


def build_tree(input, key):
    if type(key) == int:
        return key
    if key in input:
        expr = input[key][0]
        if type(expr) == int:
            return expr
        else:
            return build_tree(input, expr)
    else:
        if len(key) == 4:
            return key
        else:
            m1 = input[key[:4]][0]
            m2 = input[key[-4:]][0]
            op = key[5]

            return [build_tree(input, m1), op, build_tree(input, m2)]






def collapse(input):
    while True:
        progress = False
        for monkey in input:
            if len(input[monkey][1]) == 0 or monkey == 'root' or monkey == 'humn':
                continue
            if all(map(lambda x: len(input[x][1]) == 0, input[monkey][1])):
                progress = True
                # print(f'collapse {monkey}')
                input[monkey][0] = e(input, input[monkey][0])
                # for dep in input[monkey][1]:
                #     input[monkey][2].add(dep)
                #     input[monkey][2].update(input[dep][2])
                input[monkey][1] = []
        if not progress:
            return


def rightop(op, a, b):
    if op == '*':
        return operator.floordiv(a,b)
    elif op == '+':
        return operator.sub(a,b)
    elif op == '-':
        return operator.add(a,b)
    else:
        return operator.mul(a,b)


def leftop(op, a, b):
    if op == '*':
        return operator.floordiv(b,a)
    elif op == '+':
        return operator.sub(b,a)
    elif op == '-':
        return operator.sub(a,b)
    else:
        return operator.floordiv(a,b)

def part1(filename):
    input = parse_file(filename)
    input['humn'][0] = 'HUMN'
    input['humn'][1] = ['humn']
    collapse(input)

    expr = input['root'][0]
    print(input['root'][0])
    tree = build_tree(input, expr[:4])
    target = build_tree(input, expr[-4:])


    while len(tree) == 3:
        print(tree, '=', target)
        l, op, r = tree
        if type(l) == int:
            target = leftop(op, l, target)
            tree = r
        else:
            target = rightop(op, target, r)
            tree = l
    print(tree, '=', target)



def part2(filename):
    input = parse_file(filename)
    ans = 0
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
part1('input.txt')
# 8759966720571 too high
# 1931 too low

# part2('example.txt')
# part2('input.txt')
