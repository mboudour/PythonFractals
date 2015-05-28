import numpy as np
import matplotlib.pylab as plt
import random

def gasket(pa, pb, pc, level):
    x=(random.random(),random.random(),random.random())
    if level == 0:
        plt.fill([pa[0], pb[0], pc[0]], [pa[1], pb[1], pc[1]], color=x,alpha=0.9) 
        plt.hold(True)
    else:
        gasket(pa, (pa + pb) / 2., (pa + pc) / 2., level - 1) 
        gasket(pb, (pb + pa) / 2., (pb + pc) / 2., level - 1) 
        gasket(pc, (pc + pa) / 2., (pc + pb) / 2., level - 1)
        plt.hold(True)
        plt.fill([(pa[0] + pb[0]) / 2.,(pb[0] + pc[0]) / 2.,(pa[0] + pc[0]) / 2.],
                 [(pa[1] + pb[1]) / 2.,(pb[1] + pc[1]) / 2.,(pa[1] + pc[1]) / 2.],color=x,alpha=0.9)

A = np.array([0,28]) 
B = np.array([29,7])
C = np.array([18.5,-27])
D = np.array([-17.5,-27.5]) 
E = np.array([-29,6.5]) 
L = np.array([-7,6.5])
K = np.array([7,7])
M = np.array([11.5,-6])
N = np.array([0.5,-14.5])
O = np.array([-11,-6.5])
origin = np.array([0,-3])

level = 5
fig, ax = plt.subplots(1,figsize=(20,20)) 
gasket(A, L, K, level) 
gasket(B, K, M, level)
gasket(C, M, N, level)
gasket(D, N, O, level)
gasket(E, O, L, level)
gasket(origin, L, K, level)
gasket(origin, K, M, level)
gasket(origin, M, N, level)
gasket(origin, N, O, level)
gasket(origin, O, L, level)
plt.hold(False)
plt.title("A Randomly Colored Sierpinski Star (iterations = 5)")
ax.set_xlim(0,1.2) 
ax.set_ylim(0,1.2) 
plt.axis('equal')
plt.axis('off')
plt.show()