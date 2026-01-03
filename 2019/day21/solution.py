from helpers import *
from intcode import *

prog1 = '''NOT A T
OR T J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK
'''

prog2 = '''NOT A T
OR T J
NOT B T
OR T J
NOT C T
OR T J
AND D J
AND E T
OR H T
AND T J
RUN
'''

def run_springdroid(data, prog, debug=False):
    memory = parse(data)
    def get_input():
        for c in prog:
            yield ord(c)
    for out in run(memory, get_input(), False):
        if out > 127:
            return out
        if debug:
            print(chr(out), end='')


exec(run_springdroid, 'input.txt', prog=prog1)
exec(run_springdroid, 'input.txt', prog=prog2)
