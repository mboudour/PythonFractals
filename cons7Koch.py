import matplotlib.pylab as plt
import numpy as np
import math
import random

def koch(a,b,iteration):
    np.seterr(all='ignore')
    a1=a[0]
    a2=a[1]
    
    b1=b[0]
    b2=b[1]
    
    #a = [a1,a2]
    #b = [b1,b2]
    theta = np.arctan((b2-a2)/(b1-a1))
    length = np.sqrt((a1-b1)**2+(a2-b2)**2)
    
    c1 = (2*a1+b1)/3.
    c2 = (2*a2+b2)/3.
    c = [c1,c2]
    
    d1 = (a1+2*b1)/3.
    d2 = (a2+2*b2)/3.
    d = [d1,d2]
    
    if c1 > a1:
        m1 = c1 + (length/3.)*math.cos(theta+math.pi/3.)
        m2 = c2 + (length/3.)*math.sin(theta+math.pi/3.)
    elif c1 < a1:
        m1 = c1 + (length/3.)*math.cos(theta-2*math.pi/3.)
        m2 = c2 + (length/3.)*math.sin(theta-2*math.pi/3.)
    else:
        if c2 > a2:
            m1 = a1 - length*h/3.
            m2 = a2 + length/2.
            #print a, b, m1, m2, length
        elif c2 < a2:
            m1 = a1 + length*h/3.
            m2 = a2 - length/2.
            #print a, b, m1, m2, length
        else:
            print a1, a2, c1, c2, m1, m2, d1, d2, b1, b2
    m = [m1,m2]
    
    c = np.array(c)
    d = np.array(d)
    m = np.array(m)
    
    points = []
    
    if iteration == 0:
        points.extend([a,b])
    elif iteration == 1:
        points.extend([a, c, m, d, b])
    else:
        points.extend(koch(a,c,iteration-1))
        points.extend(koch(c,m,iteration-1))
        points.extend(koch(m,d,iteration-1))
        points.extend(koch(d,b,iteration-1))  
                        
    return points

iteration = 7

h = np.sqrt(3)/2.

# 0 Koch (center)
a=np.array([0,0])
b=np.array([1,0])
c=np.array([0.5,-h])
points0a = koch(a,b,iteration)
points0b = koch(b,c,iteration)
points0c = koch(c,a,iteration)
#points0a = koch(a=np.array([0,0]),b=np.array([1,0]),iteration=5)
#points0b = koch(a=np.array([1,0]),b=np.array([0.5,-h]),iteration=5)
#points0c = koch(a=np.array([0.5,-h]),b=np.array([0,0]),iteration=5)

points0 = []
for i in range(len(points0a)):
    points0.append(np.array(points0a[i]))
for i in range(len(points0b)):
    points0.append(np.array(points0b[i]))
for i in range(len(points0c)):
    points0.append(np.array(points0c[i]))

pts0x=[]
pts0y=[]
for i in range(len(points0)):
    pts0x.append(points0[i][0])
    pts0y.append(points0[i][1])

# 1 Koch
a=np.array([0,2*h/3.])
b=np.array([1/2.,h/3.])
c=np.array([0,0])
points1a = koch(a,b,iteration)
points1b = koch(b,c,iteration)
points1c = koch(c,a,iteration)
#points1a = koch(a=np.array([0,2*h/3.]),b=np.array([1/2.,h/3.]),iteration=5)
#points1b = koch(a=np.array([1/2.,h/3.]),b=np.array([0,0]),iteration=5)
#points1c = koch(a=np.array([0,0]),b=np.array([0,2*h/3.]),iteration=5)

points1 = []
for i in range(len(points1a)):
    points1.append(np.array(points1a[i]))
for i in range(len(points1b)):
    points1.append(np.array(points1b[i]))
for i in range(len(points1c)):
    points1.append(np.array(points1c[i]))

pts1x=[]
pts1y=[]
for i in range(len(points1)):
    pts1x.append(points1[i][0])
    pts1y.append(points1[i][1])


# 2 Koch
b=np.array([1,2*h/3.])
a=np.array([1/2.,h/3.])
c=np.array([1,0])
points2a = koch(a,b,iteration)
points2b = koch(b,c,iteration)
points2c = koch(c,a,iteration)
#points2a = koch(a=np.array([1/2.,h/3.]),b=np.array([1,2*h/3.]),iteration=5)
#points2b = koch(a=np.array([1,2*h/3.]),b=np.array([1,0]),iteration=5)
#points2c = koch(a=np.array([1,0]),b=np.array([1/2.,h/3.]),iteration=5)

points2 = []
for i in range(len(points2a)):
    points2.append(np.array(points2a[i]))
for i in range(len(points2b)):
    points2.append(np.array(points2b[i]))
for i in range(len(points2c)):
    points2.append(np.array(points2c[i]))

pts2x=[]
pts2y=[]
for i in range(len(points2)):
    pts2x.append(points2[i][0])
    pts2y.append(points2[i][1])

# 3 Koch
a=np.array([1,0])
b=np.array([3/2.,-h/3.])
c=np.array([1,-2*h/3.])
points3a = koch(a,b,iteration)
points3b = koch(b,c,iteration)
points3c = koch(c,a,iteration)
#points3a = koch(a=np.array([1,0]),b=np.array([1.5,-h/3.]),iteration=5)
#points3b = koch(a=np.array([1.5,-h/3.]),b=np.array([1,-2*h/3.]),iteration=5)
#points3c = koch(a=np.array([1,-2*h/3.]),b=np.array([1,0]),iteration=5)

points3 = []
for i in range(len(points3a)):
    points3.append(np.array(points3a[i]))
for i in range(len(points3b)):
    points3.append(np.array(points3b[i]))
for i in range(len(points3c)):
    points3.append(np.array(points3c[i]))

pts3x=[]
pts3y=[]
for i in range(len(points3)):
    pts3x.append(points3[i][0])
    pts3y.append(points3[i][1])
    
# 4 Koch
a=np.array([1/2.,-h])
b=np.array([1,-2*h/3.])
c=np.array([1,-4*h/3.])
points4a = koch(a,b,iteration)
points4b = koch(b,c,iteration)
points4c = koch(c,a,iteration)
#points4a = koch(a=np.array([1/2.,-h]),b=np.array([1,-2*h/3.]),iteration=5)
#points4b = koch(a=np.array([1,-2*h/3.]),b=np.array([1,-4*h/3.]),iteration=5)
#points4c = koch(a=np.array([1,-4*h/3.]),b=np.array([1/2.,-h]),iteration=5)

points4 = []
for i in range(len(points4a)):
    points4.append(np.array(points4a[i]))
for i in range(len(points4b)):
    points4.append(np.array(points4b[i]))
for i in range(len(points4c)):
    points4.append(np.array(points4c[i]))

pts4x=[]
pts4y=[]
for i in range(len(points4)):
    pts4x.append(points4[i][0])
    pts4y.append(points4[i][1])    
    
# 5 Koch
a=np.array([0,-2*h/3.])
b=np.array([1/2.,-h])
c=np.array([0,-4*h/3.])
points5a = koch(a,b,iteration)
points5b = koch(b,c,iteration)
points5c = koch(c,a,iteration)
#points5a = koch(a=np.array([0,-2*h/3.]),b=np.array([1/2.,-h]),iteration=5)
#points5b = koch(a=np.array([1/2.,-h]),b=np.array([0,-4*h/3.]),iteration=5)
#points5c = koch(a=np.array([0,-4*h/3.]),b=np.array([0,-2*h/3.]),iteration=5)

points5 = []
for i in range(len(points5a)):
    points5.append(np.array(points5a[i]))
for i in range(len(points5b)):
    points5.append(np.array(points5b[i]))
for i in range(len(points5c)):
    points5.append(np.array(points5c[i]))

pts5x=[]
pts5y=[]
for i in range(len(points5)):
    pts5x.append(points5[i][0])
    pts5y.append(points5[i][1])  

# 6 Koch
a=np.array([0,-2*h/3.])
b=np.array([-1/2.,-h/3.])
c=np.array([0,0])
points6a = koch(a,b,iteration)
points6b = koch(b,c,iteration)
points6c = koch(c,a,iteration)
#points6a = koch(a=np.array([0,-2*h/3.]),b=np.array([-1/2.,-h/3.]),iteration=5)
#points6b = koch(a=np.array([-1/2.,-h/3.]),b=np.array([0,0]),iteration=5)
#points6c = koch(a=np.array([0,0]),b=np.array([0,-2*h/3.]),iteration=5)

points6 = []
for i in range(len(points6a)):
    points6.append(np.array(points6a[i]))
for i in range(len(points6b)):
    points6.append(np.array(points6b[i]))
for i in range(len(points6c)):
    points6.append(np.array(points6c[i]))    
       
pts6x=[]
pts6y=[]
for i in range(len(points6)):
    pts6x.append(points6[i][0])
    pts6y.append(points6[i][1])  

fig, ax = plt.subplots(1,figsize=(20,20)) 

x0=(random.random(),random.random(),random.random())
plt.fill(pts0x, pts0y, color=x0,alpha=0.9)
plt.hold(True)

x1=(random.random(),random.random(),random.random())
plt.fill(pts1x, pts1y, color=x1,alpha=0.9)
plt.hold(True)

x2=(random.random(),random.random(),random.random())
plt.fill(pts2x, pts2y, color=x2,alpha=0.9)
plt.hold(True)

x3=(random.random(),random.random(),random.random())
plt.fill(pts3x, pts3y, color=x3,alpha=0.9)
plt.hold(True)

x4=(random.random(),random.random(),random.random())
plt.fill(pts4x, pts4y, color=x4,alpha=0.9)
plt.hold(True)

x5=(random.random(),random.random(),random.random())
plt.fill(pts5x, pts5y, color=x5,alpha=0.9)
plt.hold(True)

x6=(random.random(),random.random(),random.random())
plt.fill(pts6x, pts6y, color=x6,alpha=0.9)
plt.hold(True)

ax.set_xlim(0,3.2) 
ax.set_ylim(0,3.2) 
plt.axis('equal')
plt.axis('off')
plt.show()