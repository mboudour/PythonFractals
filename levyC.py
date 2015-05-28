import matplotlib.pyplot as plt
import argparse
import math

def L_system(level, initial_state, trgt, rplcmnt, trgt2, rplcmnt2):
    state = initial_state
   
    for counter in range(level):
        state2 = ''
        for character in state:
            if character == trgt:
                state2 += rplcmnt
            elif character == trgt2:
                state2 += rplcmnt2
            else:
                state2 += character
        state = state2
    return state

def L(angle,coords,jump):
    return angle + math.radians(45)
def R(angle,coords,jump):
    return angle - math.radians(45)
def l(angle,coords,jump):
    return angle + math.radians(45)
def r(angle,coords,jump):
    return angle - math.radians(45)

def F(angle, coords, jump):
    coords.append(
        (coords[-1][0] + jump * math.cos(angle),
         coords[-1][1] + jump * math.sin(angle)))
    return angle

def G(angle,coords,jump):
    coords.append(
        (coords[-1][0] + cosin[angle],
            coords[-1][1] +sines[angle]))
    return angle

decode = dict(L=L, R=R, F=F, G=G,l=l,r=r)

def levyc(steps, length=200, startPos=(0,0)):
    starting= 'R'*steps+'FX'
    pathcodes = L_system(steps,  'F', 'F', 'rFllFr', '', '')
    jump = float(length) / (math.sqrt(2) ** steps)
    coords = [startPos]
    angle = 0
    for move in pathcodes:
        if move == 'F' or move =='r' or move== 'l' or move == 'R':
            angle= decode[move](angle,coords,jump)
    return coords



totalwidth=100
iterations = 0

fig = plt.figure(figsize=(17,10))
points = levyc(iterations,totalwidth,(-totalwidth/2,0))

plt.subplot(2,3,1).set_title("Levy's C Curve (iterations = 0)")
    
plt.plot([p[0] for p in points], [p[1] for p in points], '-',lw=3,color='darkgreen')
plt.axis('equal')
plt.axis('off')

iterations = 1

plt.subplot(2,3,2).set_title("Levy's C Curve (iterations = 1)")

points = levyc(iterations,totalwidth,(-totalwidth/2,0))
plt.plot([p[0] for p in points], [p[1] for p in points], '-',lw=3,color='darkgreen')
plt.axis('equal')
plt.axis('off')

iterations = 2

plt.subplot(2,3,3).set_title("Levy's C Curve (iterations = 2)")

points = levyc(iterations,totalwidth,(-totalwidth/2,0))
plt.plot([p[0] for p in points], [p[1] for p in points], '-',lw=3,color='darkgreen')
plt.axis('equal')
plt.axis('off')

iterations = 3

plt.subplot(2,3,4).set_title("Levy's C Curve (iterations = 3)")

points = levyc(iterations,totalwidth,(-totalwidth/2,0))
plt.plot([p[0] for p in points], [p[1] for p in points], '-',lw=3,color='darkgreen')
plt.axis('equal')
plt.axis('off')

iterations = 4

plt.subplot(2,3,5).set_title("Levy's C Curve (iterations = 4)")

points = levyc(iterations,totalwidth,(-totalwidth/2,0))
plt.plot([p[0] for p in points], [p[1] for p in points], '-',lw=3,color='darkgreen')
plt.axis('equal')
plt.axis('off')

iterations = 5

plt.subplot(2,3,6).set_title("Levy's C Curve (iterations = 5)")

points = levyc(iterations,totalwidth,(-totalwidth/2,0))
plt.plot([p[0] for p in points], [p[1] for p in points], '-',lw=3,color='darkgreen')
plt.axis('equal')
plt.axis('off')

iterations = 20

plt.figure(figsize=(20,16))

points = levyc(iterations,totalwidth,(-totalwidth/2,0))
plt.plot([p[0] for p in points], [p[1] for p in points], '-',color='olivedrab')
plt.axis('equal')
plt.axis('off')

plt.title("Levy's C Curve (iterations = 20)")

plt.show()