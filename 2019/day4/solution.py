from collections import defaultdict, Counter

import functools
import math
import re
import sys


def check(n,allow_multiple):
    ns = str(n)
    groups = []
    group = ns[0]
    for i in range(1, len(ns), 1):
        if ns[i] < ns[i-1]:
            return 0
        if len(group) == 0 or group[0] == ns[i]:
            group += ns[i]
        else :
            groups.append(group)
            group = ns[i]
    if len(group) > 0:
        groups.append(group)
    
    if allow_multiple:
        return int(any(map(lambda x: len(x) > 1, groups)))
    return int(any(map(lambda x: len(x) == 2, groups)))


def solution(m,n):
    ans_p1 = 0
    ans_p2 = 0
    for i in range(m, n+1, 1):
        ans_p1 += check(i, True)
        ans_p2 += check(i, False)
    print(f'ans {m},{n}: {ans_p1}, {ans_p2}')



solution(245318,765747)
