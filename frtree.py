import matplotlib.pyplot as plt
import math
import argparse

def drawTree(x1, y1, angle, depth):

    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        plt.plot([x1,x2],[y1,y2],'-',color='darkgreen',lw=3)
        drawTree(x2, y2, angle - 20, depth - 1)
        drawTree(x2, y2, angle + 20, depth - 1)

# if __name__ == '__main__':
    
#     # Parse command-line args for output file name.
#     parser = argparse.ArgumentParser(description=(
#         'Creating the Fractal Tree'))
#     parser.add_argument('-a', '--angle',nargs='?', metavar='total Width', type=int,
#         default=90, help='Which Width')
#     parser.add_argument('-i', '--iterations',nargs='?', metavar='Iterations', type=int,
#         default=12, help='How many iterations')
#     parser.add_argument('-v', '--verbose', nargs='?', metavar='Verbose print', type=bool,
#         default=False, help='Print or not helping')

#     args = parser.parse_args()
#     depth=args.iterations
 
#     plt.figure(figsize=(25,20))
#     # depth=12
#     drawTree(300, 550, 45, depth)
#     drawTree(300, 550, 135, depth)
#     s="Fractal Tree (iterations = %i)" %depth
#     plt.title(s)
#     plt.axis('off')
#     plt.show()

plt.figure(figsize=(20,3))

plt.subplot(1,5,1)
depth=1
drawTree(300, 550, 90, depth)
s="Fractal Tree (iterations = %i)" %depth
plt.title(s)
plt.axis('off')

plt.subplot(1,5,2)
depth=2
drawTree(300, 550, 90, depth)
s="Fractal Tree (iterations = %i)" %depth
plt.title(s)
plt.axis('off')

plt.subplot(1,5,3)
depth=3
drawTree(300, 550, 90, depth)
s="Fractal Tree (iterations = %i)" %depth
plt.title(s)
plt.axis('off')

plt.subplot(1,5,4)
depth=4
drawTree(300, 550, 90, depth)
s="Fractal Tree (iterations = %i)" %depth
plt.title(s)
plt.axis('off')

plt.subplot(1,5,5)
depth=5
drawTree(300, 550, 90, depth)
s="Fractal Tree (iterations = %i)" %depth
plt.title(s)
plt.axis('off')

plt.figure(figsize=(25,20))
depth=12
drawTree(300, 550, 90, depth)
#drawTree(300, 550, 45, depth)
#drawTree(300, 550, 135, depth)
s="Fractal Tree (iterations = %i)" %depth
plt.title(s)
plt.axis('off')

plt.show()