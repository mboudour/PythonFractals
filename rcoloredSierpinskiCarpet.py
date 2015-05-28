import numpy as np
import matplotlib.pylab as plt
import random

def carpet(a, b, c, d, iterations, offset=np.array([0,0])):

    ab = (a + b)/3.
    ba = 2*(a + b)/3.
    bc = (2*b + c)/3.
    cb = (b + 2*c)/3.
    dc = (c + 2*d)/3.
    cd = (2*c + d)/3.
    ad = (d + a)/3.
    da = 2*(d + a)/3.

    abd = 2*a/3. + (b + d)/3.
    bac = a + (2*b + d)/3.
    cbd = 4*a/3. + 2*(b + d)/3.
    dac = a + (b + 2*d)/3.

    x=(random.random(),random.random(),random.random())

    plt.fill([abd[0]+offset[0], bac[0]+offset[0],
    cbd[0]+offset[0], dac[0]+offset[0]],
                 [abd[1]+offset[1], bac[1]+offset[1],
    cbd[1]+offset[1], dac[1]+offset[1]], color=x,alpha=0.9)
    plt.hold(True)
    
    if iterations == 0:
        plt.fill([abd[0]+offset[0], bac[0]+offset[0],
        cbd[0]+offset[0], dac[0]+offset[0]],
                 [abd[1]+offset[1], bac[1]+offset[1],
            cbd[1]+offset[1], dac[1]+offset[1]], color=x,alpha=0.9)
        plt.hold(True)
        
    else:
        
        #1
        a_m =np.array([0,0])
        ab_m = ab - a
        abd_m = abd - a
        ad_m = ad - a
        offset1= offset +a
        carpet(a_m, ab_m, abd_m, ad_m, iterations - 1,offset1)

        #2
        ab_m =np.array([0,0])
        ba_m = ba - ab
        bac_m = bac - ab
        abd_m = abd - ab
        offset2= offset +ab
        carpet(ab_m, ba_m, bac_m, abd_m, iterations - 1,offset2)

        #3
        ba_m =np.array([0,0])
        b_m = b - ba
        bc_m = bc - ba
        bac_m = bac - ba
        offset3= offset +ba
        carpet(ba_m, b_m, bc_m, bac_m, iterations - 1,offset3)

        #4
        bac_m =np.array([0,0])
        bc_m = bc - bac
        cb_m = cb - bac
        cbd_m = cbd - bac
        offset4= offset +bac
        carpet(bac_m, bc_m, cb_m, cbd_m, iterations - 1,offset4)

        #5
        cbd_m = np.array([0, 0])
        cb_m = cb - cbd
        c_m = c - cbd
        cd_m = cd - cbd
        offset5= offset +cbd
        carpet(cbd_m, cb_m, c_m, cd_m, iterations - 1,offset5)

        
        #6
        dac_m = np.array([0, 0])
        cbd_m = cbd - dac
        cd_m = cd - dac
        dc_m = dc - dac
        offset6= offset +dac
        carpet(dac_m, cbd_m, cd_m, dc_m, iterations - 1,offset6)
        
        
        #7
        da_m = np.array([0, 0])
        dac_m = dac - da
        dc_m = dc - da
        d_m = d - da
        offset7= offset +da
        carpet(da_m, dac_m, dc_m, d_m, iterations - 1,offset7)
        
        
        #8
        ad_m = np.array([0, 0])
        abd_m = abd - ad
        dac_m = dac - ad
        da_m = da - ad
        offset8= offset +ad
        carpet(ad_m, abd_m, dac_m, da_m, iterations - 1,offset8)

a = np.array([0, 0])
b = np.array([3, 0])
c = np.array([3, 3])
d = np.array([0, 3])

iterations = 4

plt.figure(figsize=(20,20))

plt.fill([a[0],b[0],c[0],d[0]],[a[1],b[1],c[1],d[1]],color='maroon',alpha=0.8)
plt.hold(True)

carpet(a, b, c, d, iterations)

plt.title("Randomly Colored Sierpinski Carpet (iterations = 4)")
plt.axis('equal')
plt.axis('off')
plt.show()