import numpy as np
import matplotlib.pylab as plt

def bis(x,y,k):
    return (y - x)/float(k) + x   
    
def f(a,b,c,k): 
    return bis(a,b,k), bis(b,c,k), bis(a,c,k)
    
def Sierpinski(a,b,c,k,iteration): 
    if iteration==0:
        plt.fill([a[0], b[0], c[0]], [a[1], b[1], c[1]],'b') 
        plt.hold(True)
    else:
        Sierpinski(a,bis(a,b,k),bis(a,c,k),k,iteration-1)
        Sierpinski(b,bis(a,b,k),bis(b,c,k),k,iteration-1)
        Sierpinski(c,bis(a,c,k),bis(b,c,k),k,iteration-1)
        plt.hold(True)

a = np.array([0,0])
b = np.array([1,0])
c = np.array([0.5,np.sqrt(3)/2.])

k = 3

plt.figure(figsize=(15,15))

iterations = 5

Sierpinski(a, b, c, k, iterations)

plt.title("Asymmetrical (cut at 1/3) Sierpinski Triangle (iterations = 5)")
plt.axis('equal')
plt.axis('off')
plt.show()