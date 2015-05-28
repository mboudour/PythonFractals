import matplotlib.pylab as plt
import numpy as np
import math

from Koch_line import koch

h = np.sqrt(3)/2.
a = np.array([0, 0])
b = np.array([1, 0])
c = np.array([0.5, h])

iterations = 7

points1 = koch(a=np.array([0, 0]),b=np.array([1,0]),iterations=iterations)
points2 = koch(a=np.array([1, 0]),b=np.array([0.5,-h]),iterations=iterations)
points3 = koch(a=np.array([0.5, -h]),b=np.array([0,0]),iterations=iterations)

points = []
for i in range(len(points1)):
    points.append(np.array(points1[i]))
for i in range(len(points2)):
    points.append(np.array(points2[i]))
for i in range(len(points3)):
    points.append(np.array(points3[i]))

ptsx=[]
ptsy=[]
for i in range(len(points)):
    ptsx.append(points[i][0])
    ptsy.append(points[i][1])

plt.figure(figsize=(25,25))

plt.title("Koch Triangle (iterations = 7)")
plt.plot(ptsx, ptsy, '-')
plt.fill(ptsx, ptsy, color='lightcyan',alpha=0.7)
plt.axis('equal')
plt.axis('off')
plt.show()