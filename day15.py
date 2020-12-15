import math
import re
import sys

def run(filename):
  with open(filename, 'r') as f:
    nums = [int(n) for n in f.readline().split(',')]
    turns = {}
    for i in range(len(nums)):
      n = nums[i]
      turns[n] = [i, 0]
    print(turns)

    last = nums[-1]
    num = 0

    for i in range(len(nums), 30000000):
      if turns[last][1] > 0:
        # print(turns[last])
        num = turns[last][1]
        if num in turns:
          last_turn = turns[num][0]
          turns[num][0] = i
          turns[num][1] = i - last_turn
        else:
          turns[num] = [i, 0]
      else:
        num = 0
        last_turn = turns[num][0]
        turns[num][0] = i
        turns[num][1] = i - last_turn

      last = num
      if i % 1000000 == 0:
        print(i)
    print(num)



# run('day15_ex.txt')
run('day15.txt') # 1876406