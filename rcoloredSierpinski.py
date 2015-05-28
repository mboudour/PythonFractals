import numpy as np
import matplotlib.pylab as plt
import random

def sierpinski(a, b, c, iterations):
    x=(random.random(),random.random(),random.random())
    if iterations  == 0:
        plt.fill([a[0], b[0], c[0]], [a[1], b[1], c[1]], color=x,alpha=0.9) 
        plt.hold(True)
    else:
        sierpinski(a, (a + b) / 2., (a + c) / 2., iterations  - 1) 
        sierpinski(b, (b + a) / 2., (b + c) / 2., iterations  - 1) 
        sierpinski(c, (c + a) / 2., (c + b) / 2., iterations  - 1)
        plt.fill([(a[0] + b[0]) / 2., (a[0] + c[0]) / 2., (b[0] + c[0]) / 2.], [(a[1] + b[1]) / 2., (a[1] + c[1]) / 2., (b[1] + c[1]) / 2.], color=x,alpha=0.9)

a = np.array([0, 0])
b = np.array([1, 0])
c = np.array([0.5, np.sqrt(3)/2.])

plt.figure(figsize=(15,15))

iterations = 6

sierpinski(a, b, c, iterations)

plt.title("Randomly Colored Sierpinski Triangle (iterations = 6)")
plt.axis('equal')
plt.axis('off')
plt.show()