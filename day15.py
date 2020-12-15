import math
import re
import sys

def run(filename):
  with open(filename, 'r') as f:
    for line in f:
      line = line.strip()
      print(line)

run('day15_ex.txt')
# run('day15.txt')