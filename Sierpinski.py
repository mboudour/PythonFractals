# coding: utf-8

import numpy as np
import matplotlib.pylab as plt

def SierpinskiTriangle(a, b, c, iterations):
    '''
    Recursively generated Sierpinski Triangle. 
    '''
    if iterations == 0:
        # Fill the triangle with vertices a, b, c. 
        plt.fill([a[0], b[0], c[0]], [a[1], b[1], c[1]], 'g') 
        plt.hold(True)
    else:
        # Recursive calls for the three subtriangles. 
        SierpinskiTriangle(a, (a + b) / 2., (a + c) / 2., iterations - 1) 
        SierpinskiTriangle(b, (b + a) / 2., (b + c) / 2., iterations - 1) 
        SierpinskiTriangle(c, (c + a) / 2., (c + b) / 2., iterations - 1)
        
a = np.array([0, 0])
b = np.array([1, 0])
c = np.array([0.5, np.sqrt(3)/2.])

iterations = 0

fig = plt.figure(figsize=(15,15))
plt.subplot(2,3,1).set_title("Sierpinski Triangle (iterations = 0)")

SierpinskiTriangle(a, b, c, iterations)

plt.axis('equal')
plt.axis('off')

iterations = 1

plt.subplot(2,3,2).set_title("Sierpinski Triangle (iterations = 1)")

SierpinskiTriangle(a, b, c, iterations)

plt.axis('equal')
plt.axis('off')

iterations = 2

plt.subplot(2,3,3).set_title("Sierpinski Triangle (iterations = 2)")

SierpinskiTriangle(a, b, c, iterations)

plt.axis('equal')
plt.axis('off')

iterations = 3

plt.subplot(2,3,4).set_title("Sierpinski Triangle (iterations = 3)")

SierpinskiTriangle(a, b, c, iterations)

plt.axis('equal')
plt.axis('off')

iterations = 4

plt.subplot(2,3,5).set_title("Sierpinski Triangle (iterations = 4)")

SierpinskiTriangle(a, b, c, iterations)

plt.axis('equal')
plt.axis('off')

iterations = 5

plt.subplot(2,3,6).set_title("Sierpinski Triangle (iterations = 5)")

SierpinskiTriangle(a, b, c, iterations)

plt.axis('equal')
plt.axis('off')

iterations = 6

plt.figure(figsize=(25,25))

SierpinskiTriangle(a, b, c, iterations)

plt.title("Sierpinski Triangle (iterations = 6)")
plt.axis('equal')
plt.axis('off')
plt.show()