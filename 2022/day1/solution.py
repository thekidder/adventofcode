from helpers import *

def parse_file(filename):
    return grouped_input(filename, int)

def solution(filename):
    cals = [sum(x) for x in parse_file(filename)]
    cals.sort()
    print(cals[-1])
    print(sum(cals[-3:]))

solution('example.txt')
solution('input.txt')
