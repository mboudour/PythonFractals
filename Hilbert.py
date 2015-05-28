import sys, math
import numpy as np
import matplotlib.pyplot as plt
  
def hilbert(x0, y0, xi, xj, yi, yj, n,points):
    if n <= 0:
        X = x0 + (xi + yi)/2
        Y = y0 + (xj + yj)/2
        points.append((X,Y))
    else:
        hilbert(x0,               y0,               yi/2, yj/2, xi/2, xj/2, n - 1,points)
        hilbert(x0 + xi/2,        y0 + xj/2,        xi/2, xj/2, yi/2, yj/2, n - 1,points)
        hilbert(x0 + xi/2 + yi/2, y0 + xj/2 + yj/2, xi/2, xj/2, yi/2, yj/2, n - 1,points)
        hilbert(x0 + xi/2 + yi,   y0 + xj/2 + yj,  -yi/2,-yj/2,-xi/2,-xj/2, n - 1,points)
        return points

        
# def main():
#     args = sys.stdin.readline()
#     # Remain the loop until the renderer releases the helper...
#     while args:
#         arg = args.split()
#         # Get the inputs
#         pixels = float(arg[0])
#         ctype = arg[1]
#         reps = int(arg[2])
#         width = float(arg[3])
        
#         # Calculate the number of curve cv's
#         cvs = int(math.pow(4, reps))
            
#         # Begin the RenderMan curve statement
#         print 'Basis \"b-spline\" 1 \"b-spline\" 1'
#         print 'Curves \"%s\" [%s] \"nonperiodic\" \"P\" [' % (ctype, cvs)
    
#         # Create the curve
#         hilbert(0.0, 0.0, 1.0, 0.0, 0.0, 1.0, reps)
    
#         # End the curve statement
#         print '] \"constantwidth\" [%s]' % width
      
#         # Tell the renderer we have finished   
#         sys.stdout.write('\377')
#         sys.stdout.flush()
        
#         # read the next set of inputs
#         args = sys.stdin.readline()
# if __name__ == "__main__":
#     main()

a = np.array([0, 0])
b = np.array([1, 0])
c = np.array([1, 1])
d = np.array([0, 1])
ab = (a + b)/2.
bc = (b + c)/2.
cd = (c + d)/2.
ad = (d + a)/2.
aab = (a + ab)/2.
bba = (b + ab)/2.
aad = (a + ad)/2.
dda = (d + ad)/2.
ccb = (c + bc)/2.
bbc = (b + bc)/2.
ccd = (c + cd)/2.
ddc = (d + cd)/2.

iterations = 1

fig = plt.figure(figsize=(17,17))
plt.subplot(2,3,1).set_title("Hilbert Curve (iterations = 1)")

points = hilbert(0.0, 0.0, 1.0, 0.0, 0.0, 1.0, iterations,[])
plt.plot([p[0] for p in points], [p[1] for p in points], '-',lw=3,color='darkmagenta')

plt.plot([a[0],b[0],c[0],d[0],a[0]],[a[1],b[1],c[1],d[1],a[1]],'k-',lw=1)
plt.plot([ab[0],cd[0]],[ab[1],cd[1]],'k--',lw=1)
plt.plot([ad[0],bc[0]],[ad[1],bc[1]],'k--',lw=1)
plt.plot([b[0],c[0]],[b[1],c[1]],'k-',lw=3)

plt.axis('equal')
plt.axis('off')

iterations = 2

plt.subplot(2,3,2).set_title("Hilbert Curve (iterations = 2)")

points = hilbert(0.0, 0.0, 1.0, 0.0, 0.0, 1.0, iterations,[])
plt.plot([p[0] for p in points], [p[1] for p in points], '-',lw=3,color='darkmagenta')#,lw=5)

plt.plot([a[0],b[0],c[0],d[0],a[0]],[a[1],b[1],c[1],d[1],a[1]],'k-',lw=1)
plt.plot([ab[0],cd[0]],[ab[1],cd[1]],'k--',lw=1)
plt.plot([ad[0],bc[0]],[ad[1],bc[1]],'k--',lw=1)
plt.plot([b[0],c[0]],[b[1],c[1]],'k-',lw=3)

plt.axis('equal')
plt.axis('off')

iterations = 3

plt.subplot(2,3,3).set_title("Hilbert Curve (iterations = 3)")

points = hilbert(0.0, 0.0, 1.0, 0.0, 0.0, 1.0, iterations,[])
plt.plot([p[0] for p in points], [p[1] for p in points], '-',lw=3,color='darkmagenta')#,lw=5)

plt.plot([a[0],b[0],c[0],d[0],a[0]],[a[1],b[1],c[1],d[1],a[1]],'k-',lw=1)
plt.plot([ab[0],cd[0]],[ab[1],cd[1]],'k--',lw=1)
plt.plot([ad[0],bc[0]],[ad[1],bc[1]],'k--',lw=1)
plt.plot([b[0],c[0]],[b[1],c[1]],'k-',lw=3)
plt.plot([aab[0],ddc[0]],[aab[1],ddc[1]],'k--',lw=1)
plt.plot([bba[0],ccd[0]],[bba[1],ccd[1]],'k--',lw=1)
plt.plot([aad[0],bbc[0]],[aad[1],bbc[1]],'k--',lw=1)
plt.plot([dda[0],ccb[0]],[dda[1],ccb[1]],'k--',lw=1)

plt.axis('equal')
plt.axis('off')

iterations = 4

plt.subplot(2,3,4).set_title("Hilbert Curve (iterations = 4)")

points = hilbert(0.0, 0.0, 1.0, 0.0, 0.0, 1.0, iterations,[])
plt.plot([p[0] for p in points], [p[1] for p in points], '-',lw=3,color='darkmagenta')#,lw=5)

plt.axis('equal')
plt.axis('off')

iterations = 5

plt.subplot(2,3,5).set_title("Hilbert Curve (iterations = 5)")

points = hilbert(0.0, 0.0, 1.0, 0.0, 0.0, 1.0, iterations,[])
plt.plot([p[0] for p in points], [p[1] for p in points], '-',lw=3,color='darkmagenta')#,lw=5)

plt.axis('equal')
plt.axis('off')
iterations = 6

plt.subplot(2,3,6).set_title("Hilbert Curve (iterations = 6)")

points = hilbert(0.0, 0.0, 1.0, 0.0, 0.0, 1.0, iterations,[])
plt.plot([p[0] for p in points], [p[1] for p in points], '-',lw=3,color='darkmagenta')#,lw=5)

plt.axis('equal')
plt.axis('off')

fig = plt.figure(figsize=(25,25))

points = hilbert(0.0, 0.0, 1.0, 0.0, 0.0, 1.0, iterations,[])
plt.plot([p[0] for p in points], [p[1] for p in points], '-',lw=3,color='darkmagenta')#,lw=5)
plt.title("Hilbert Curve (iterations = 7)")
plt.axis('equal')
plt.axis('off')

plt.show()