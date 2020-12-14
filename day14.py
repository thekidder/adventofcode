import re

mem = {}

def run(filename):
  with open(filename, 'r') as f:
    onesmask = 0
    zerosmask = 68719476735
    for line in f:
      line = line.strip()
      if line.startswith('mask = '):
        onesmask = 0
        zerosmask = 0
        mask = line[-36:]
        print(mask)
        for i in range(len(mask)):
          bit = mask[-i - 1]
          if bit == '1':
            # print(f'1 bit at {i}')
            onesmask += 1 << i
          if bit == '0':
            # print(f'0 bit at {i}')
            zerosmask += 1 << i
        # print(onesmask)
        # print(zerosmask)
      else:
        m = re.match('mem\[(\d+)\] \= (\d+)', line)
        g = m.groups()
        addr = int(g[0])
        val = int(g[1])
        # print(val & zerosmask)

        mem[addr] = (val | onesmask) ^ (val & zerosmask)
        print(addr, mem[addr])

  s = 0
  for addr, val in mem.items():
    s += val
  print(mem)
  print(s)
  # NOT 9889493670975

# run('day14_ex.txt')
run('day14.txt')