import numpy as np
import matplotlib.pylab as plt


def vicsek(a, b, c, d, iterations, offset=np.array([0,0])):

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


    if iterations == 0:
        plt.fill([ab[0]+offset[0],ba[0]+offset[0],bac[0]+offset[0],bc[0]+offset[0],
        cb[0]+offset[0],cbd[0]+offset[0],cd[0]+offset[0],dc[0]+offset[0],dac[0]+offset[0],
        da[0]+offset[0],ad[0]+offset[0],abd[0]+offset[0]],
        [ab[1]+offset[1],ba[1]+offset[1],bac[1]+offset[1],bc[1]+offset[1],
        cb[1]+offset[1],cbd[1]+offset[1],cd[1]+offset[1],dc[1]+offset[1],
        dac[1]+offset[1],da[1]+offset[1],ad[1]+offset[1],abd[1]+offset[1]],
        'saddlebrown')
        plt.hold(True)
    else:
        #1
        abd_m =np.array([0,0])
        bac_m = bac - abd
        cbd_m = cbd - abd
        dac_m = dac - abd
        offset1= offset +abd
        vicsek(abd_m, bac_m, cbd_m, dac_m, iterations - 1,offset1)

        #2
        ab_m =np.array([0,0])
        ba_m = ba - ab
        bac_m = bac - ab
        abd_m = abd - ab
        offset2= offset +ab
        vicsek(ab_m, ba_m, bac_m, abd_m, iterations - 1,offset2)

        # #3
        # ba_m =np.array([0,0])
        # b_m = b - ba
        # bc_m = bc - ba
        # bac_m = bac - ba
        # offset3= offset +ba
        # vicsek(ba_m, b_m, bc_m, bac_m, iterations - 1,offset3)

        #3
        bac_m =np.array([0,0])
        bc_m = bc - bac
        cb_m = cb - bac
        cbd_m = cbd - bac
        offset4= offset +bac
        vicsek(bac_m, bc_m, cb_m, cbd_m, iterations - 1,offset4)

        # #5
        # cbd_m = np.array([0, 0])
        # cb_m = cb - cbd
        # c_m = c - cbd
        # cd_m = cd - cbd
        # offset5= offset +cbd
        # vicsek(cbd_m, cb_m, c_m, cd_m, iterations - 1,offset5)

        
        #4
        dac_m = np.array([0, 0])
        cbd_m = cbd - dac
        cd_m = cd - dac
        dc_m = dc - dac
        offset6= offset +dac
        vicsek(dac_m, cbd_m, cd_m, dc_m, iterations - 1,offset6)
        
        
        # #7
        # da_m = np.array([0, 0])
        # dac_m = dac - da
        # dc_m = dc - da
        # d_m = d - da
        # offset7= offset +da
        # vicsek(da_m, dac_m, dc_m, d_m, iterations - 1,offset7)
        
        
        #5
        ad_m = np.array([0, 0])
        abd_m = abd - ad
        dac_m = dac - ad
        da_m = da - ad
        offset8= offset +ad
        vicsek(ad_m, abd_m, dac_m, da_m, iterations - 1,offset8)

a = np.array([0, 0])
b = np.array([3, 0])
c = np.array([3, 3])
d = np.array([0, 3])

fig = plt.figure(figsize=(10,10))

iterations = 0

plt.subplot(2,2,1).set_title("Vicsek Fractal (iterations = 0)")

vicsek(a, b, c, d, iterations)

plt.axis('equal')
plt.axis('off')


iterations = 1

plt.subplot(2,2,2).set_title("Vicsek Fractal (iterations = 1)")

vicsek(a, b, c, d, iterations)

plt.axis('equal')
plt.axis('off')


iterations = 2

plt.subplot(2,2,3).set_title("Vicsek Fractal (iterations = 2)")

vicsek(a, b, c, d, iterations)

plt.axis('equal')
plt.axis('off')


iterations = 3

plt.subplot(2,2,4).set_title("Vicsek Fractal (iterations = 3)")

vicsek(a, b, c, d, iterations)

plt.axis('equal')
plt.axis('off')

iterations = 5

plt.figure(figsize=(20,20))
vicsek(a, b, c, d, iterations)
#plt.hold(False)
plt.title("Vicsek Fractal (iterations = 5)")
plt.axis('equal')
plt.axis('off')

plt.show()