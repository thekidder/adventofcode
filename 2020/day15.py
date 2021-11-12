def run(filename):
  with open(filename, 'r') as f:
    nums = [int(n) for n in f.readline().split(',')]
    turns = {}
    for i in range(len(nums)):
      n = nums[i]
      turns[n] = [i, 0]

    last = nums[-1]
    num = 0

    for i in range(len(nums), 30000000):
      num = turns[last][1]

      if num in turns:
        turns[num][1] = i - turns[num][0]
        turns[num][0] = i
      else:
        turns[num] = [i, 0]

      last = num
      if i % 1000000 == 0:
        print(i)
    print(num)


# run('day15_ex.txt')
run('day15.txt') # 1876406