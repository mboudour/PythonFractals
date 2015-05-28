import matplotlib.pylab as plt
import numpy as np
import math

def koch(a,b,iterations):

    a1=a[0]
    a2=a[1]
    
    b1=b[0]
    b2=b[1]
    
    theta = np.arctan((b2-a2)/(b1-a1))
    length = np.sqrt((a1-b1)**2+(a2-b2)**2)
    
    c1 = (2*a1+b1)/3.
    c2 = (2*a2+b2)/3.
    c = [c1,c2]
    
    d1 = (a1+2*b1)/3.
    d2 = (a2+2*b2)/3.
    d = [d1,d2]
    
    if c1 >= a1:
        m1 = c1 + (length/3.)*math.cos(theta+math.pi/3.)
        m2 = c2 + (length/3.)*math.sin(theta+math.pi/3.)
    else:
        m1 = c1 + (length/3.)*math.cos(theta-2*math.pi/3.)
        m2 = c2 + (length/3.)*math.sin(theta-2*math.pi/3.)
    m = [m1,m2]
    
    c = np.array(c)
    d = np.array(d)
    m = np.array(m)
    
    points = []
    
    if iterations == 0:
        points.extend([a,b])
    elif iterations == 1:
        points.extend([a, c, m, d, b])
    else:
        points.extend(koch(a,c,iterations-1))
        points.extend(koch(c,m,iterations-1))
        points.extend(koch(m,d,iterations-1))
        points.extend(koch(d,b,iterations-1))  
                        
    return points



fig = plt.figure(figsize=(15,5))

plt.subplot(2,3,1).set_title("Koch Line (iterations = 0)")
points = koch(a=np.array([0, 0]),b=np.array([1,0]),iterations=0)
ptsx=[]
ptsy=[]
for i in range(len(points)):
    ptsx.append(points[i][0])
    ptsy.append(points[i][1])
plt.plot(ptsx, ptsy, '-')
plt.axis('equal')
plt.axis('off')

plt.subplot(2,3,2).set_title("Koch Line (iterations = 1)")
points = koch(a=np.array([0, 0]),b=np.array([1,0]),iterations=1)
ptsx=[]
ptsy=[]
for i in range(len(points)):
    ptsx.append(points[i][0])
    ptsy.append(points[i][1])
plt.plot(ptsx, ptsy, '-')
plt.axis('equal')
plt.axis('off')

plt.subplot(2,3,3).set_title("Koch Line (iterations = 2)")
points = koch(a=np.array([0, 0]),b=np.array([1,0]),iterations=2)
ptsx=[]
ptsy=[]
for i in range(len(points)):
    ptsx.append(points[i][0])
    ptsy.append(points[i][1])
plt.plot(ptsx, ptsy, '-')
plt.axis('equal')
plt.axis('off')

plt.subplot(2,3,4).set_title("Koch Line (iterations = 3)")
points = koch(a=np.array([0, 0]),b=np.array([1,0]),iterations=3)
ptsx=[]
ptsy=[]
for i in range(len(points)):
    ptsx.append(points[i][0])
    ptsy.append(points[i][1])
plt.plot(ptsx, ptsy, '-')
plt.axis('equal')
plt.axis('off')


plt.subplot(2,3,5).set_title("Koch Line (iterations = 4)")
points = koch(a=np.array([0, 0]),b=np.array([1,0]),iterations=4)
ptsx=[]
ptsy=[]
for i in range(len(points)):
    ptsx.append(points[i][0])
    ptsy.append(points[i][1])
plt.plot(ptsx, ptsy, '-')
plt.axis('equal')
plt.axis('off')

plt.subplot(2,3,6).set_title("Koch Line (iterations = 5)")
points = koch(a=np.array([0, 0]),b=np.array([1,0]),iterations=5)
ptsx=[]
ptsy=[]
for i in range(len(points)):
    ptsx.append(points[i][0])
    ptsy.append(points[i][1])
plt.plot(ptsx, ptsy, '-')
plt.axis('equal')
plt.axis('off')




plt.figure(figsize=(25,7))

plt.title("Koch Line (iterations = 6)")
points = koch(a=np.array([0, 0]),b=np.array([1,0]),iterations=6)
ptsx=[]
ptsy=[]
for i in range(len(points)):
    ptsx.append(points[i][0])
    ptsy.append(points[i][1])
plt.plot(ptsx, ptsy, '-')
plt.axis('equal')
plt.axis('off')
plt.show()