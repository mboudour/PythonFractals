import numpy as np
import matplotlib.pylab as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import math
import random

from collections import namedtuple

Circle = namedtuple('Circle', ['cen', 'rad'])
Line   = namedtuple('Line', ['end1', 'end2'])

import matplotlib.pyplot as plt

def draw_line(ax, line, colour='b', linewidth=2):
    """
    Draw a line object on an axis
    """
    ax.plot([line.end1[0],line.end2[0]],[line.end1[1],line.end2[1]],color=colour,linewidth=linewidth)
    
    return


def draw_circle(ax, circle, colour='r', linewidth=2):
    """
    Draw a circle object on an axis
    """
    circle_artist = plt.Circle(circle.cen,circle.rad,color=colour,fill=True,linewidth=linewidth)
    ax.add_artist(circle_artist)
    
    return








def circle_in_three_circles(circ1, circ2, circ3):
    """
    Find the small Soddy circle for three existing circles
    """
    
    # Bends
    b1 = 1./circ1.rad
    b2 = 1./circ2.rad
    b3 = 1./circ3.rad
    
    # Solve Descartes circle theorem
    bs = b1 + b2 + b3 + 2*np.sqrt( b1*b2 + b2*b3 + b3*b1 )
    radius = 1./bs
    
    # Centre-bend products
    z1 = b1 * complex(circ1.cen[0],circ1.cen[1])
    z2 = b2 * complex(circ2.cen[0],circ2.cen[1])
    z3 = b3 * complex(circ3.cen[0],circ3.cen[1])
    
    # Solve complex Descartes circle theorem - two solutions
    zspos = z1 + z2 + z3 + 2*np.sqrt( z1*z2 + z2*z3 + z3*z1 )
    zsneg = z1 + z2 + z3 - 2*np.sqrt( z1*z2 + z2*z3 + z3*z1 )
    
    # Possible centres
    centrepos = zspos/bs
    centreneg = zsneg/bs
    
    # See which one is closer to fitting 
    errpos = abs(np.linalg.norm(np.array(circ1.cen)-np.array([centrepos.real,centrepos.imag]))-(radius+circ1.rad)) \
           + abs(np.linalg.norm(np.array(circ2.cen)-np.array([centrepos.real,centrepos.imag]))-(radius+circ2.rad)) \
           + abs(np.linalg.norm(np.array(circ3.cen)-np.array([centrepos.real,centrepos.imag]))-(radius+circ3.rad))
    errneg = abs(np.linalg.norm(np.array(circ1.cen)-np.array([centreneg.real,centreneg.imag]))-(radius+circ1.rad)) \
           + abs(np.linalg.norm(np.array(circ2.cen)-np.array([centreneg.real,centreneg.imag]))-(radius+circ2.rad)) \
           + abs(np.linalg.norm(np.array(circ3.cen)-np.array([centreneg.real,centreneg.imag]))-(radius+circ3.rad))
    
    # Choose one
    if errneg > errpos:
        centre = centrepos
    else:
        centre = centreneg
    
    # Make a circle object
    soddy_circle = Circle((centre.real,centre.imag),radius)
    
    return soddy_circle 


def circle_in_two_circles_and_a_line(circ1, circ2, line):
    """
    Find the Soddy circle for two existing circles and a tangent line
    """
    
    # Bends
    b1 = 1./circ1.rad
    b2 = 1./circ2.rad
    
    # Solve Descartes circle theorem
    bs = b1 + b2 + 2*np.sqrt( b1*b2 )
    radius = 1./bs
    
    # Centre-bend products
    z1 = b1 * complex(circ1.cen[0],circ1.cen[1])
    z2 = b2 * complex(circ2.cen[0],circ2.cen[1])
    
    # Limiting centre-bend
    vec = np.array(line.end2)-np.array(line.end1)
    unit_vec = vec/np.linalg.norm(vec)
    z3 = complex(-unit_vec[1],unit_vec[0])
    
    # Solve complex Descartes circle theorem - two solutions
    zspos = z1 + z2 + z3 + 2*np.sqrt( z1*z2 + z2*z3 + z3*z1 )
    zsneg = z1 + z2 + z3 - 2*np.sqrt( z1*z2 + z2*z3 + z3*z1 )
    
    # Possible centres
    centrepos = zspos/bs
    centreneg = zsneg/bs
    
    # See which one is closer to fitting 
    errpos = abs(np.linalg.norm(np.array(circ1.cen)-np.array([centrepos.real,centrepos.imag]))-(radius+circ1.rad)) \
           + abs(np.linalg.norm(np.array(circ2.cen)-np.array([centrepos.real,centrepos.imag]))-(radius+circ2.rad))
    errneg = abs(np.linalg.norm(np.array(circ1.cen)-np.array([centreneg.real,centreneg.imag]))-(radius+circ1.rad)) \
           + abs(np.linalg.norm(np.array(circ2.cen)-np.array([centreneg.real,centreneg.imag]))-(radius+circ2.rad))
    
    # Choose one
    if errneg > errpos:
        centre = centrepos
    else:
        centre = centreneg
    
    # Make a circle object
    soddy_circle = Circle((centre.real,centre.imag),radius)
    
    return soddy_circle 



def circle_in_two_lines_and_a_circle(line1, line2, circle):
    """
    Find the incircle between two converging lines and a tangent circle
    """
    
    # See if the lines need switching round
    if line2.end1 != line1.end2:
        tmpline = line2
        line2 = line1
        line1 = tmpline
    
    # Get the centre and radius of the circle and the vertex where the lines meet
    point = np.array(line1.end2)
    centre = np.array(circle.cen)
    radius = np.array(circle.rad)
    
    # Find a unit vector pointing from the centre to the vertex
    vector1 = point-centre
    vectorlength = np.linalg.norm(vector1)
    vector1 = vector1/vectorlength
    
    # Find the intersection point where the helper line is tangent to the circle
    intersect = centre + radius*vector1
    
    # Find the half-length of the helper line
    halflength = radius/np.sqrt( 1 + 2*radius/(vectorlength-radius) )
    
    # Rotate the unit vector so it points along the helper line
    vector2 = np.dot(np.array([[0,-1],[1,0]]),vector1)
    
    # Find the ends of the helper line
    end1 = tuple(intersect - halflength*vector2)
    end2 = tuple(intersect + halflength*vector2)
    helper_line = Line(end1,end2)
    
    # Make shortened copies of the other two lines
    shortline1 = Line(end2, line1.end2)
    shortline2 = Line(line2.end1, end1)
    
    # Call the existing incircle routine
    incircle = circle_in_three_lines(shortline1, shortline2, helper_line)
    
    return incircle
    


def circle_in_three_lines(line1, line2, line3):
    """
    Find the incircle of a triangle specified by three lines
    """
    
    # End point coordinates
    xa = line1.end1[0]
    ya = line1.end1[1]
    xb = line2.end1[0]
    yb = line2.end1[1]
    xc = line3.end1[0]
    yc = line3.end1[1]
    
    # Lengths
    la = np.linalg.norm(np.array([xc-xb,yc-yb]))
    lb = np.linalg.norm(np.array([xa-xc,ya-yc]))
    lc = np.linalg.norm(np.array([xb-xa,yb-ya]))
    
    # Semiperimeter
    s = 0.5*(la+lb+lc)
    
    # Incircle radius
    ri = np.sqrt((s-la)*(s-lb)*(s-lc)/s)
    
    # Incentre
    xi = (la*xa + lb*xb + lc*xc)/(2*s)
    yi = (la*ya + lb*yb + lc*yc)/(2*s)
    
    # Make incircle
    incircle = Circle((xi,yi),ri)
    
    return incircle

class TriangleError(ValueError):
    """
    Invalid triangle specification
    """

def convert_triangle(triangle):
    """
    Convert a list of three 2D points representing a triangle into a set of sides.
    Raise an error if the triangle is not a triangle.
    """
    
    # Make sure it has exactly three corners
    if len(triangle) != 3:
        raise TriangleError("Triangle must have three corners")
    
    # Get corners
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]
    
    # Make sure each corner has two coordinates
    if ((len(a)!=2) or (len(b)!=2) or (len(c)!=2)):
        raise TriangleError("Corners must have two coordinates")
        
    try:
        # Make sides from corners, taking care of the sign
        if ( (b[0]-a[0])*(c[1]-b[1]) - (b[1]-a[1])*(c[0]-b[0]) ) < 0:
            line1 = Line(a,b)
            line2 = Line(b,c)
            line3 = Line(c,a)
        else:
            line1 = Line(a,c)
            line2 = Line(c,b)
            line3 = Line(b,a)
            
    except TypeError:
        raise TriangleError("Corners are not valid numbers")
        

    sides = [line1,line2,line3]
    
    return sides

from collections import deque

def pack_circles_in_triangle(triangle, radius_limit):
    """
    Recursively pack circles into a triangle
    """
    
    # Convert triangle (3 points) into a set of side
    sides = convert_triangle(triangle)
    
    # Create a circle list
    circle_list = list(sides)
    counter = 2
    
    # Create a to-do stack
    todo_list = deque([(0,1,2)])
    
    # Loop
    it = 0
    while todo_list:
        it += 1
        
        # What's next
        parents = todo_list.popleft()
        
        # How many lines are present
        num_lines = 0
        for ii in range(3):
            if parents[ii] < 3:
                num_lines += 1
        
        # Switch on number of lines
        if num_lines == 0:
            
            # Three circles
            circle1 = circle_list[parents[0]]
            circle2 = circle_list[parents[1]]
            circle3 = circle_list[parents[2]]
            
            # Spawn a new circle
            new_circle = circle_in_three_circles(circle1, circle2, circle3)
            
        elif num_lines == 1:
            
            # Two circles, one line
            line1 = circle_list[parents[0]]
            circle1 = circle_list[parents[1]]
            circle2 = circle_list[parents[2]]
            
            # Spawn a new circle
            new_circle = circle_in_two_circles_and_a_line(circle1, circle2, line1)
            
        elif num_lines == 2:
            
            # Two lines, one circle
            line1 = circle_list[parents[0]]
            line2 = circle_list[parents[1]]
            circle1 = circle_list[parents[2]]
            
            # Spawn a new circle
            new_circle = circle_in_two_lines_and_a_circle(line1, line2, circle1)
            
        elif num_lines == 3:
            
            # Three line
            line1 = circle_list[parents[0]]
            line2 = circle_list[parents[1]]
            line3 = circle_list[parents[2]]
            
            # Spawn a new circle
            new_circle = circle_in_three_lines(line1, line2, line3)
            
        else:
            raise ValueError
        
        if new_circle.rad > radius_limit:
        
            # Add the new circle to the list
            circle_list.append(new_circle)
            counter += 1
            
            # Add a new parent combinations to the to-do stack
            todo_list.append((parents[0],parents[1],counter))
            todo_list.append((parents[0],parents[2],counter))
            todo_list.append((parents[1],parents[2],counter))
    
    
    # Remove the three lines from the list
    circle_list[:3] = []
    
    return sides,circle_list


def draw_triangle_fractal(ax, triangle, radius_limit, linecolour='w', circlecolour='r', linewidth=2):
    #linecolour='k'
    """
    Draw a triangle and pack circles in it.
    """
    sides,circle_list = pack_circles_in_triangle(triangle, radius_limit)
    
    for ii in range(3):
        draw_line(ax, sides[ii], colour=linecolour, linewidth=linewidth)
    
    for circle in circle_list:
        circlecolour=(random.random(),random.random(),random.random())
        draw_circle(ax, circle, colour=circlecolour, linewidth=linewidth)
    
    return

import numpy as np

triangle = [(0,0), (1,0), (0.5, np.sqrt(3)/2.)]    #[(-2,-2),(0,2),(2,0)]

#triangle = [(0,0), (1,0), (0,1)]

radius_limit = 0.005
fig = plt.figure(figsize=(18,18))
ax = fig.add_subplot(1,1,1)
ax.set_xlim((0,1))  #((-3,3))
ax.set_ylim((0,1))     #((-3,3))

draw_triangle_fractal(ax, triangle, radius_limit)

plt.axis('off')
plt.show()