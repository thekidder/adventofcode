import functools
import sys 
nums = []

with open('day10.txt', 'r') as f:
  for line in f:
    nums.append(int(line))

nums.append(0)
nums.sort()
nums.append(nums[-1]+3)

threes = 0
ones = 0

for i in range(1, len(nums)):
  if nums[i] - nums[i-1] == 1:
    ones +=1
  elif nums[i] - nums[i-1] == 3:
    threes += 1
  else:
    print('!!!: ' + str(nums[i-1]) + ', ' + str(nums[i]))

print(ones * threes)

chain_lens = [1]
for i in range(1, len(nums)):
  chain_lens.append(0)

for i in range(1, len(nums)):
  for j in range(0, 3):
    if i + j < len(nums) and nums[i+j] - nums[i-1] <= 3:
      chain_lens[i+j] += chain_lens[i-1]

print(chain_lens[-1])