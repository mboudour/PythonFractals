import numpy as np
import matplotlib.pylab as plt
import random

def bis(x,y,k):
    return (y - x)/float(k) + x

def f(a,b,c,k):
    return bis(a,b,k), bis(b,c,k), bis(a,c,k)

def Sierpinski(a,b,c,k,iteration): 
    
    x=(random.random(),random.random(),random.random())
    if iteration==0:
        plt.fill([a[0], b[0], c[0]], [a[1], b[1], c[1]],color=x,alpha=0.9)
        plt.hold(True)
        
    else:
        Sierpinski(a,bis(a,b,k),bis(a,c,k),k,iteration-1)
        Sierpinski(b,bis(a,b,k),bis(b,c,k),k,iteration-1)
        Sierpinski(c,bis(a,c,k),bis(b,c,k),k,iteration-1)
        plt.hold(True)
        
        plt.fill([bis(a,b,k)[0], bis(a,c,k)[0], bis(b,c,k)[0]],
[bis(a,b,k)[1], bis(a,c,k)[1], bis(b,c,k)[1]], color=x,alpha=0.9)

h = np.sqrt(3)

a1 = np.array([0,0])
b1 = np.array([3,0])
c1 = np.array([1.5,h])
a1u = np.array([0,2*h])
b1u = np.array([3,2*h])
c1u = np.array([1.5,h])

a2 = np.array([0,0])
b2 = np.array([0,2*h])
c2 = np.array([1.5,h])
a2r = np.array([3,0])
b2r = np.array([3,2*h])
c2r = np.array([1.5,h])

k1 = 3
k1u = 5
k2 = 4
k2r = 6

fig, ax = plt.subplots(1,figsize=(30,30)) 

Sierpinski(a1,b1,c1,k1,iteration=7) 
plt.hold(True)
Sierpinski(a1u,b1u,c1u,k1u,iteration=7) 
plt.hold(True)
Sierpinski(a2,b2,c2,k2,iteration=7) 
plt.hold(True)
Sierpinski(a2r,b2r,c2r,k2r,iteration=7) 
plt.hold(True)

plt.title("A Cubistic Sierpinski Synthesis (iterations = 7)")
ax.set_xlim(0,1) 
ax.set_ylim(0,1) 
plt.axis('equal')
plt.axis('off')
plt.show()