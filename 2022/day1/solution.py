import functools
from helpers import *

def parse_file(filename):
    return grouped_input(filename, int)

def solution(filename):
    cals = [functools.reduce(add, x) for x in parse_file(filename)]
    cals.sort()
    print(cals[-1])
    print(functools.reduce(add, cals[-3:]))

solution('example.txt')
solution('input.txt')
