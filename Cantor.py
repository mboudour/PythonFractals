import numpy as np
import matplotlib.pylab as plt
import argparse

def cantor(n):
    return [0.] + cant(0., 1., n) + [1.]

def cant(x, y, n):
    if n == 0:
        return []

    new_pts = [2.*x/3. + y/3., x/3. + 2.*y/3.]
    return cant(x, new_pts[0], n-1) + new_pts + cant(new_pts[1], y, n-1)

def plotcant(points,iterations):
	fig, ax = plt.subplots(1,figsize=(20,2)) 
	for k,v in points.items():
		y = [(iterations-k)*0.1,(iterations-k)*0.1]
		for i in range(0,len(v),2):
			x = [v[i],v[i+1]]
			# print i,i+1
			plt.plot(x,y,'-b',linewidth=3) 
	s = "The Cantor Ternary Set (iterations = "+str(iterations)+")"
 	plt.title(s)
	ax.set_xlim(0,1) 
	ax.set_ylim(0,1) 
	# plt.axis('equal')
	plt.axis('off')
	plt.show()


if __name__ == '__main__':
    
    # Parse command-line args for output file name.
    parser = argparse.ArgumentParser(description=(
        'Creating the Cantor ternary set'))
    parser.add_argument('-j', '--jintervals',nargs='?', metavar='Iterations', type=int,
        default=1, help='Which interval to remove')
    parser.add_argument('-i', '--iterations',nargs='?', metavar='Iterations', type=int,
        default=1, help='How many iterations')
    parser.add_argument('-v', '--verbose', nargs='?', metavar='Verbose print', type=bool,
        default=False, help='Print or not helping')

    args = parser.parse_args()
    iterations=args.iterations
    verbose=args.verbose
    points = dict()

    for i in range(args.iterations):
    	# print i, cantor(i)
    	if args.jintervals ==1:
    		points[i] = cantor(i)
    	elif args.jintervals ==2:
    		points[i] = cantor4(i)

    print points
    plotcant(points,args.iterations)


    

