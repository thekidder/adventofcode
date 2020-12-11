import functools
import sys 
nums = []

with open('day9.txt', 'r') as f:
  for line in f:
    nums.append(int(line))

# def valid(i):
#   nums_to_consider = nums[i-25:i]
#   for j in range(0, len(nums_to_consider)):
#     for k in range(j + 1, len(nums_to_consider)):
#       # print(nums_to_consider[j], nums_to_consider[k])
#       if nums_to_consider[j] + nums_to_consider[k] == nums[i]:
#         return True
#   return False

# for i in range(27, len(nums)):
#   if not valid(i):
#     print(i)
#     print(nums[i])
#     sys.exit(0)
#   # print(len(nums_to_consider))
#   # print(nums[i])

target = 466456641

def add(x,y): return x+y

for i in range(len(nums)):
  for j in range(i+1, len(nums)+1):
    r = nums[i:j]
    sum = functools.reduce(add, r)
    if sum == target:
      x = sorted(r)
      print(x[0] + x[-1])
      sys.exit(0)
    elif sum > target:
      break