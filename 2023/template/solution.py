from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import random
import sys

import numpy as np
# from scipy import optimize
from scipy.optimize import fsolve,least_squares

from helpers import *

# regex example
pattern = re.compile('(-?\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            nums = pattern.findall(line)
            pos = tuple(map(int, nums[:3]))
            vel = tuple(map(int, nums[3:]))
            lines.append((pos,vel))

    return lines


def part1(filename):
    input = parse_file(filename)
    ans = 0
    for i,j in itertools.combinations(input, 2):
        p1 = i[0][:2]
        p2 = vadd(p1, i[1][:2])

        p3 = j[0][:2]
        p4 = vadd(p3, j[1][:2])
        print(p1,p2,p3,p4)

        dem = (p1[0] - p2[0])*(p3[1]-p4[1])-(p1[1]-p2[1])*(p3[0]-p4[0])

        if dem == 0:
            continue
        num1 = (p1[0]*p2[1] - p1[1]*p2[0])*(p3[0]-p4[0])-(p1[0]-p2[0])*(p3[0]*p4[1]-p3[1]*p4[0])
        num2 = (p1[0]*p2[1] - p1[1]*p2[0])*(p3[1]-p4[1])-(p1[1]-p2[1])*(p3[0]*p4[1]-p3[1]*p4[0])

        xint = num1/dem
        yint = num2/dem

        intmin = 7
        intmax = 27
        intmin = 200000000000000
        intmax = 400000000000000

        slope1 = i[1][1] / i[1][0] 
        slope2 = j[1][1] / j[1][0]

        b1 = p1[1] - slope1*p1[0]
        b2 = p3[1] - slope2*p3[0]

        print(b1,b2,slope1,slope2)

        x1 = (yint - b1)/slope1 - p1[0]
        x2 = (yint - b2)/slope2 - p3[0]

        print(x1,x2)

        if i[1][0] < 0:
            x1 = -x1
        if j[1][0] < 0:
            x2 = -x2

        print(x1,x2)

        if x1 < 0 or x2 < 0:
            continue

        print(xint,yint)

        if xint >= intmin and yint >= intmin and xint <= intmax and yint <= intmax:
            ans += 1

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    # random.shuffle(input)
    # print(input)

    # for v in generate_velocity():
    #     for i in input[1:]:

    # values = np.array([])

    # bounds = optimize.Bounds(-np.inf, np.inf)
    # integrality = np.full_like(values, True) 

    n = len(input)

    def f(x):
        p = x[:3]
        v = x[3:6]
        t = x[6:]

        # n_eqns = len(input) + 6 # 11 for example
        eqns = []
        for i in range(len(input)): # 1 - 4
            for j in range(3):
                eqns.append(t[i]*input[i][1][j] + input[i][0][j] - (t[i]*v[j] + p[j]))
        # for i in x:
        #     ip, fp = math.modf(i)
        #     eqns.append(fp)
        return eqns#[:n_eqns]

    guess = [input[0][0][0]+1,input[0][0][1]+1,input[0][0][2]+1,1,1,1] + [1]*n#list(range(1, n+1))
    # guess = [24,13,10, -3,1,2, 5,3,4,6,1]
    bounds = (
        # [-np.inf, -np.inf, -np.inf, -1000, -1000, -1000] + [1] * n,
        # [np.inf, np.inf, np.inf, 1000, 1000, 1000] + [np.inf] * n,
        [-4000000000000000] * 3 + [-1000000] * 3 + [0] * n,
        [ 4000000000000000] * 3 + [1000000] * 3 + [10000000000] * n,
    )
    res = least_squares(f, guess, bounds=bounds,method='dogbox',jac='cs')
    print('STATUS', res.success, res.status)
    # roots = list(map(round, res.x))
    roots = list(map(round, res.x))
    # roots = res.x
    print(roots)
    # print(list(map(int, roots)))
    ans = roots[0] + roots[1] + roots[2]

    print(roots[0] + roots[3]*roots[6]) #prx + vrx * t1 
    print(input[0][0][0] + input[0][1][0]*roots[6]) #p1x + v1x * t1 


    # constraints = optimize.LinearConstraint(A=eqns, lb=0, ub=capacity)

    # res = milp(c=-values, constraints=constraints,
    #        integrality=integrality, bounds=bounds) 
            

    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

part2('example.txt')
# too high 836739974338902
# too high 754362884530662
# too high 754362884532830
part2('input.txt')
