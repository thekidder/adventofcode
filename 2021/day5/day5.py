import collections
import math
import re
import sys

line_pattern = re.compile('([\d]+),([\d]+) -> ([\d]+),([\d]+)')

def part1(file):
    lines = []
    
    with open(file, 'r') as f:
        for line in f:
            m = line_pattern.match(line)
            if m is None:
                print('ERROR')
                break
            x1 = int(m.group(1))
            y1 = int(m.group(2))

            x2 = int(m.group(3))
            y2 = int(m.group(4))

            lines.append((x1,y1,x2,y2))

        grid = collections.defaultdict(int)
        for line in lines:
            x1,y1,x2,y2 = line
            if x1 != x2 and y1 != y2:
                continue


            step_x = 0
            step_y = 0

            if x1 != x2:
                step_x = int(math.copysign(1, x2-x1))
            else:
                step_y = int(math.copysign(1, y2-y1))

            # print(x1,x2,y1,y2)
            while x1 != x2 or y1 != y2:
                # print(x1, y1)
                grid[(x1, y1)] += 1
                # print(grid[(x1, y1)])
                x1 += step_x
                y1 += step_y
            grid[(x1, y1)] +=1
            # print(x1, y1)


            # if x1 == x2:
            #     print(x1,x2,y1,y2)
            #     for y in range(y1, y2+1, ):
            #         print(x1, y)
            #         grid[(x1, y)] +=1
            #     sys.exit(0)
            # else:
            #     for x in range(x1, x2+1, int(math.copysign(1, y2-y1))):
            #         grid[(x, y1)] +=1

        cnt = 0
        for pos, val in grid.items():
            if val > 1:
                cnt += 1

        print(cnt)

    # print(lines)

def part2(file):
    lines = []
    
    with open(file, 'r') as f:
        for line in f:
            m = line_pattern.match(line)
            if m is None:
                print('ERROR')
                break
            x1 = int(m.group(1))
            y1 = int(m.group(2))

            x2 = int(m.group(3))
            y2 = int(m.group(4))

            lines.append((x1,y1,x2,y2))

        grid = collections.defaultdict(int)
        for line in lines:
            x1,y1,x2,y2 = line

            step_x = 0
            step_y = 0

            if x1 != x2:
                step_x = int(math.copysign(1, x2-x1))
            if y1 != y2:
                step_y = int(math.copysign(1, y2-y1))

            while x1 != x2 or y1 != y2:
                grid[(x1, y1)] += 1
                x1 += step_x
                y1 += step_y
            grid[(x1, y1)] +=1

        cnt = 0
        for pos, val in grid.items():
            if val > 1:
                cnt += 1

        print(cnt)





part2('input.txt')