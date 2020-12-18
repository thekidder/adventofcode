import collections
import math

def next(expr):
  expr = expr.strip()
  if len(expr) > 0:
    return expr[0]
  else:
    return ''

def calc(expr, indent = ''):
  print(f'{indent}CALC {expr}')
  i = 0
  res = 0
  val = 0
  op = '+'
  while i < len(expr):
    token = expr[i]
    if len(token.strip()) == 0:
      pass
    elif token >= '0' and token <= '9':
      val = int(token)
      print(f'{indent}res = {res}, val = {val}, op = {op}')
      if op == '*':
        cnt = 0
        j = i+1
        while j < len(expr):
          if expr[j] == ' ':
            pass
          elif expr[j] == '(':
            cnt += 1
          elif expr[j] == ')':
            cnt -= 1
          if expr[j] in ['*', ')'] and cnt == 0 and j == next(expr[j:]) != '+':
            if expr[j] == ')':
              j += 1
            break
          j += 1
        print(f'{indent}MULT SUBEXPR: {expr[i+1:j]}')
        val = calc(expr[i+1:j], indent + '  ')
        res *= val
        i = j
        print(f'{indent}MULT after subexpr: {res}')
      else:
        res += val
    elif token in ['*','+']:
      op = token
      if op == '*':
        cnt = 0
        j = i+1
        while j < len(expr):
          if expr[j] == ' ':
            pass
          elif expr[j] == '(':
            cnt += 1
          elif expr[j] == ')':
            cnt -= 1
          if expr[j] in ['*', ')'] and cnt == 0 and j == next(expr[j:]) != '+':
            if expr[j] == ')':
              j += 1
            break
          j += 1
        print(f'{indent}MULT SUBEXPR: {expr[i+1:j]}')
        val = calc(expr[i+1:j], indent + '  ')
        res *= val
        i = j
        print(f'{indent}MULT after subexpr: {res}')

    elif token == '(':
      cnt = 0
      for j in range(i, len(expr)):
        if expr[j] == '(':
          cnt += 1
        elif expr[j] == ')':
          cnt -= 1
          if cnt == 0:
            val = calc(expr[i+1:j], indent + '  ')
            if op == '*':
              res *= val
            else:
              res += val
            i = j
            print(f'{indent}after subexpr: {res}')
            break
    elif token == ')':
      print('ERROR')
    else:
      print('ERROR')
    i += 1

  # if token == '*':
  #   res *= val
  # else:
  #   res += val

  print(f'{indent}CALC return {res}')
  return res

def run(filename):
  sum = 0
  with open(filename, 'r') as f:
    for line in f:
      line = line.strip()
      r = calc(line)
      sum += r

  print(sum)
# 
# print(calc('4 + (5 + (5 * 5 + 3 + 2) + (6 + 4 * 9 * 2 * 8) * 6 + (7 * 5 * 2) * (2 * 8 * 2)) + (8 * 7 + 7) * 6 * 9 * (5 + 9)'))

run('day18.txt')