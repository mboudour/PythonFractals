import turtle
import math
t = turtle.Pen()
t.tracer(100)

TOTAL_SIZE     = 10
BRANCH_ANGLE   = 50 # old 50
LEAN_ANGLE     = 2
SCALING_FACTOR_CHILDREN = 0.32 # old 0.31
SCALING_FACTOR_MAIN     = 0.9
BREAK_CASE = 1
SEGMENT_RATIOS = [0.3, 0.6]


'''
1 = 80(0.31^n)
1/80 = 0.31^n
n = log_0.31(x/80)
'''


def crazy(n): return math.log(n/80.0)/math.log(SCALING_FACTOR_CHILDREN)

def fern(size, angle):
    """Draw a fern.

    size  -- the size of the current fern (arbitrary units)
    angle -- the fern's leaning direction. -1 signifies left lean, 1 signifies
             right lean.

    """
    if size > BREAK_CASE:

        oldWidth = t.width()
        t.width(crazy(BREAK_CASE) - crazy(size))
        
        # draw the right branch
        t.forward(size * SEGMENT_RATIOS[0])
        t.right(BRANCH_ANGLE * angle)

        # we draw the new child fern; note that the angle is now reversed
        fern(size * SCALING_FACTOR_CHILDREN, -angle)
        t.left(BRANCH_ANGLE * angle)

        # draw the left branch
        t.forward(size * SEGMENT_RATIOS[1])
        t.left(BRANCH_ANGLE * angle)
        # we draw the new child fern; the angle is the same as this one
        fern(size * SCALING_FACTOR_CHILDREN, angle)
        t.right(BRANCH_ANGLE * angle)

        # draw the continuation of the current branch
        # we create the leaning effect by turning slightly in our lean direction
        t.right(LEAN_ANGLE * angle)
        fern(size * SCALING_FACTOR_MAIN, angle)
        t.left(LEAN_ANGLE * angle)

        # and backtrace all the way to the start of the fern!
        t.backward(size * sum(SEGMENT_RATIOS))

        t.width(oldWidth)

t.up(); t.goto(0, -340); t.down()
t.left(90)
t.color("darkgreen")

fern(90, 1)  #90, 1

t.tracer(1)
raw_input()