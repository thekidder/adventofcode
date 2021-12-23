-345,-311,381
-447,-329,318
-485,-357,347
-537,-823,-458
-618,-824,-621
-661,-816,-575
390,-675,-793
404,-588,-901
423,-701,434
459,-707,401
528,-643,409
544,-627,-890

(-345, -311, 381)
(-447, -329, 318)
(-485, -357, 347)
(-537, -823, -458)
(-618, -824, -621)
(-661, -816, -575)
(390, -675, -793)
(404, -588, -901)
(423, -701, 434)
(459, -707, 401)
(528, -643, 409)
(544, -627, -890)

# (-1,-2, 3)
# (-1, 2,-3)
# (-1,-3,-2)
# (-1, 3, 2)
# (-2,-1,-3)
# (-2, 1, 3)
# (-2,-3, 1)
# (-2, 3,-1)
# (-3,-1, 2)
# (-3, 1,-2)
# (-3,-2,-1)
# (-3, 2, 1)
# ( 1,-2,-3)
# ( 1, 2, 3)
# ( 1,-3, 2)
# ( 1, 3,-2)
# ( 2,-1, 3)
# ( 2, 1,-3)
# ( 2,-3,-1)
# ( 2, 3, 1)
# ( 3,-1,-2)
# ( 3, 1, 2)
# ( 3,-2, 1)
# ( 3, 2,-1)

# -1,-2, 3
# -1, 2,-3
#  1,-2,-3
#  1, 2, 3

import math
import itertools

cosines = [1,0,-1,0]
sines = [0,1,0,-1]


def mult(mat, pos):
    return (
        mat[0][0]*pos[0] + mat[0][1]*pos[1] + mat[0][2]*pos[2],
        mat[1][0]*pos[0] + mat[1][1]*pos[1] + mat[1][2]*pos[2],
        mat[2][0]*pos[0] + mat[2][1]*pos[1] + mat[2][2]*pos[2]
    )

def rotx(pos, ind):
    mat = [[1,0,0],[0, cosines[ind],-sines[ind]],[0, sines[ind],cosines[ind]]]
    return mult(mat, pos)


def roty(pos, ind):
    mat = [[cosines[ind],0,sines[ind]],[0, 1, 0],[-sines[ind], 0, cosines[ind]]]
    return mult(mat, pos)


def rotz(pos, ind):
    mat = [[cosines[ind], -sines[ind], 0], [sines[ind], cosines[ind], 0], [0, 0, 1]]
    return mult(mat, pos)


rots = [rotx,roty,rotz]

def orientations(pos):
    all = set()
    for rotation in itertools.product(range(4),repeat=3):
        output = pos[:]
        for index, amt in enumerate(rotation):
            output = rots[index](output, amt)
        all.add(output)
        # yield output
    
    for r in all:
        yield r

o = []
for x in orientations((1,2,3)):
    o.append((
        (math.copysign(1, x[0]), abs(x[0]) - 1),
        (math.copysign(1, x[1]), abs(x[1]) - 1),
        (math.copysign(1, x[2]), abs(x[2]) - 1),
    ))

print(o)