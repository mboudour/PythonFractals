from numpy import *
from matplotlib import pyplot as plt

def mandelbrot( h,w, maxit=40): #20
        '''
        Returns an image of the Mandelbrot fractal of size (h,w).
        '''
        y,x = ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
        #y,x = ogrid[ -0.25:0.25:h*1j, -1.8:-1.3:w*1j ]
        #y,x = ogrid[ -0.05:0.05:h*1j, -1.5:-1.4:w*1j ]
        c = x+y*1j
        z = c
        divtime = maxit + zeros(z.shape, dtype=int)
        for i in xrange(maxit):
                z  = z**2 + c
                diverge = z*conj(z) > 2**2            # who is diverging
                div_now = diverge & (divtime==maxit)  # who is diverging now
                divtime[div_now] = i  +100                # note when
                z[diverge] = 2                        # avoid diverging too much

        return divtime
def mandelbrot2( h,w,a=-2.,b=.8,c=-1.4,d=1.4, maxit=40): #20
        '''
        Returns an image of the Mandelbrot fractal of size (h,w).
        '''
        y,x = ogrid[ c:d:h*1j, a:b:w*1j ]
        # y,x = ogrid[ -0.25:0.25:h*1j, -1.8:-1.3:w*1j ]
        #y,x = ogrid[ -0.05:0.05:h*1j, -1.5:-1.4:w*1j ]
        c = x+y*1j
        z = c
        divtime = maxit + zeros(z.shape, dtype=int)
        for i in xrange(maxit):
                z  = z**2 + c
                diverge = z*conj(z) > 2**2            # who is diverging
                div_now = diverge & (divtime==maxit)  # who is diverging now
                divtime[div_now] = i  +100                # note when
                z[diverge] = 2                        # avoid diverging too much

        return divtime

#fig = plt.figure(figsize=(15,15))
plt.figure(figsize=(20,20))

#fig = plt.subplot(4,1,1)#,figsize=(20,20))

plt.imshow(mandelbrot2(1000,1000)) 
#s = "The Mandelbrot Set ([-2.0,0.8]x[-1.4,1.4], iterations = 40)"
#s = "The Mandelbrot Set ([-1.8,-1.3]x[-0.25,0.25], iterations = 40)"
s = "The Mandelbrot Set ([-1.5,-1.4]x[-0.05,0.05], iterations = 40)" 
#plt.subplot(4,1,1).
plt.title(s)
plt.axis('off')

##fig = plt.figure(figsize=(15,15))
##fig = plt.subplot(4,1,2)

# plt.figure(figsize=(20,20))

# plt.imshow(mandelbrot2(1000,1000,-1.8,-1.3,-.25,0.25)) 
# s = "The Mandelbrot Set ([-1.8,-1.3]x[-0.25,0.25], iterations = 40)"
# #plt.subplot(4,1,2).
# plt.title(s)
# plt.axis('off')

# plt.figure(figsize=(20,20))

# #fig = plt.figure(figsize=(15,15))
# #fig = plt.subplot(4,1,3)

# plt.imshow(mandelbrot2(1000,1000,-1.5,-1.4,-0.05,0.05)) 
# s = "The Mandelbrot Set ([-1.5,-1.4]x[-0.05,0.05], iterations = 40)"
# #plt.subplot(4,1,3).
# plt.title(s)
# plt.axis('off')

# plt.figure(figsize=(20,20))

#fig = plt.figure(figsize=(15,15))
#fig = plt.subplot(4,1,4)

plt.imshow(mandelbrot2(1000,1000,-1.,-.6,0.,0.4)) 
s = "The Mandelbrot Set ([0,0.4]x[-1.,-0.6], iterations = 40)"
#plt.subplot(4,1,4).
plt.title(s)
plt.axis('off')



plt.show()