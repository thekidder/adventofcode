from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *
from intcode import *



def part1(filename):
    code = parse(file(filename))
    ans = 0

    def get_input():
        return 0

    prog = run(code, get_input, False)
    buf = []
    for output in prog:
        buf.append(output)
        if len(buf) == 3:
            if buf[2] == 2:
                ans += 1
            buf = []

    print(f'P1 {filename}: {ans}')


def part2(filename):
    code = parse(file(filename))
    code[0] = 2
    paddle_x = None
    ball_x = None
    score = None

    def get_input():
        joystick = sign(ball_x - paddle_x)
        # print(f'providing input {joystick} (paddle at {paddle_x}, ball at {ball_x})')
        return joystick

    prog = run(code, get_input, False)
    buf = []
    for output in prog:
        buf.append(output)
        if len(buf) == 3:
            if buf[0] == -1 and buf[1] == 0:
                # print(f'got new score {buf[2]}')
                score = buf[2]
            elif buf[2] == 4:
                ball_x = buf[0]
            elif buf[2] == 3:
                paddle_x = buf[0]
            buf = []
    
    print(f'P2 {filename}: {score}')


part1('input.txt')
part2('input.txt')
