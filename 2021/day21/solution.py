import itertools
from collections import defaultdict, Counter

import re
import math
import sys

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def roll_deterministic():
    counter = 1
    while True:
        yield counter
        counter += 1
        if counter == 101:
            counter = 1

def get_space(space, roll_func):
    space += roll_func.__next__()
    space += roll_func.__next__()
    space += roll_func.__next__()

    space = ((space - 1) % 10) + 1

    return space

def part1():
    # game = [4, 8]
    game = [10, 7]
    scores = [0,0]
    ans = 0

    rolls = 0
    rollfn = roll_deterministic()
    while True:
        game[0] = get_space(game[0], rollfn)
        scores[0] += game[0]
        rolls += 3

        if scores[0] >= 1000:
            ans = scores[1] * rolls
            break

        game[1] = get_space(game[1], rollfn)
        scores[1] += game[1]
        rolls += 3

        if scores[1] >= 1000:
            ans = scores[0] * rolls
            break
        print(f'game {game} scores {scores} rolls {rolls}')
    print(f'ANSWER: {scores} {rolls} ::: {ans}')


# def get_space(roll)

def roll_dirac(space):
    spaces = []
    scores = [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 3, 1), (1, 3, 2), (1, 3, 3), (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 3, 1), (2, 3, 2), (2, 3, 3), (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 3, 1), (3, 3, 2), (3, 3, 3)]
    for score in scores:
        final_score = sum(score)
        s = space + final_score
        s = ((s - 1) % 10) + 1
        spaces.append(s)
    return spaces


def get_outcomes(game, n):
    if game[2] >= 21 or game[3] >= 21:
        c = Counter()
        c[game] = n
        return c
    outcomes = Counter()
    for space in roll_dirac(game[0]):
        p1_space = space
        p1_score = game[2] + space
        outcomes[(p1_space, game[1], p1_score, game[3])] += n

    p2_outcomes = Counter()
    for outcome, m in outcomes.items():
        if outcome[2] >= 21:
            p2_outcomes[outcome] += m
        else:
            for space in roll_dirac(outcome[1]):
                p2_space = space
                p2_score = outcome[3] + space
                p2_outcomes[(outcome[0], p2_space, outcome[2], p2_score)] += m

    return p2_outcomes

def part2():
    games = Counter()
    # games[(4,8,0,0)] = 1
    games[(10,7,0,0)] = 1
    ans = 0

    rolls = 0
    done = False
    while not done:
    # for i in range(3):
        done = True
        next = Counter()
        for game,n in games.items():
            if game[2] < 21 and game[3] < 21:
                done = False
            # if game[2] >= 21 or game[3] >= 21:
            #     next[game] = n
            #     continue
            next += get_outcomes(game, n)
            # for outcome,m in outcomes.items():
            #     next[outcome] += m
            # next[game] -= n
        games = next
        # print(games)
        print(f'UNIVERSES: {games.total()}')
        
    p1_wins = 0
    p2_wins = 0
    for game,n in games.items():
        if game[2] >= 21:
            p1_wins += n
        else:
             p2_wins += n

    print(f'ANSWER: {p1_wins,p2_wins}')


part2()
