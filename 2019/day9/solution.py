from intcode import *

def file(filename):
    with open(filename, 'r') as f:
        return f.read()


# print([x for x in run(parse('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'), [], False)])
# print([x for x in run(parse('1102,34915192,34915192,7,4,7,99,0'), [], False)])
# print([x for x in run(parse('104,1125899906842624,99'), [], False)])

# print([x for x in run(parse(file('input.txt')), [1], True)])

print([x for x in run(parse(file('input.txt')), [2], False)])
