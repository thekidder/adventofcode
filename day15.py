import math
import re
import sys

def run(filename):
  with open(filename, 'r') as f:
    nums = [int(n) for n in f.readline().split(',')]
    turns = {}
    for i in range(len(nums)):
      n = nums[i]
      turns[n] = [i]
    print(turns)

    last = nums[-1]
    num = 0

    for i in range(len(nums), 30000000):
      if len(turns[last]) > 1:
        # print(turns[last])
        num = turns[last][-1] - turns[last][-2]
        if num in turns:
          turns[num].append(i)
        else:
          turns[num] = [i]
      else:
        num = 0
        turns[0].append(i)
      # print(num)
      if len(turns[num]) > 2:
        turns[num] = turns[num][-2:]

      last = num
      if i % 100000 == 0:
        print(i)
      if i == 30000000 - 1:
        print(num)



# run('day15_ex.txt')
run('day15.txt')