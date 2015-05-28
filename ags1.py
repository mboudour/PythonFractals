#! /usr/bin/python3

# Command line program to create svg apollonian circles

# Copyright (c) 2014 Ludger Sandig
# This file is part of apollon.

# Apollon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Apollon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Apollon.  If not, see <http://www.gnu.org/licenses/>.


import argparse
import sys
import math
import numpy as np
from apollon import ApollonianGasket
from coloring import ColorMap, ColorScheme
import matplotlib.pyplot as plt
import random
def parseArguments(argv, colors):
    description = "Generate Apollonian Gaskets and save as svg"
    name = argv[0]

    colors.append('none')
    colors.sort()

    parser = argparse.ArgumentParser(description=description, prog=name)

    parser.add_argument("-d", "--depth", metavar="D", type=int, default=3, help="Recursion depth, generates 2*3^{D+1} circles. Usually safe for D<=10. For higher D use --force if you know what you are doing.")
    parser.add_argument("-o", "--output", metavar="", type=str, default="", help="Output file name. If left blank, default is created from circle curvatures.")
    parser.add_argument("-r", "--radii", action="store_true", default=False, help="Interpret c1, c2, c3 as radii and not as curvatures")
    parser.add_argument("--color", choices=colors, metavar='SCHEME', default='none', help="Color Scheme. Choose from "+", ".join(colors))
    parser.add_argument("--treshold", metavar='T', default=0.005, type=float, help="Don't save circles that are too small. Useful for higher depths to reduce filesize.")
    parser.add_argument("--force", action="store_true", default=False, help="Use if you want a higher recursion depth than 10.")

    parser.add_argument("c1", type=float, help="Curvature of first circle")
    parser.add_argument("c2", type=float, help="Curvature of second circle")
    parser.add_argument("c3", type=float, help="Curvature of third circle")

    return parser.parse_args()
def circles_C(x, y, s, c='b', ax=None, vmin=None, vmax=None, **kwargs):
    """
    Make a scatter of circles plot of x vs y, where x and y are sequence 
    like objects of the same lengths. The size of circles are in data scale.

    Parameters
    ----------
    x,y : scalar or array_like, shape (n, )
        Input data
    s : scalar or array_like, shape (n, ) 
        Radius of circle in data scale (ie. in data unit)
    c : color or sequence of color, optional, default : 'b'
        `c` can be a single color format string, or a sequence of color
        specifications of length `N`, or a sequence of `N` numbers to be
        mapped to colors using the `cmap` and `norm` specified via kwargs.
        Note that `c` should not be a single numeric RGB or
        RGBA sequence because that is indistinguishable from an array of
        values to be colormapped.  `c` can be a 2-D array in which the
        rows are RGB or RGBA, however.
    ax : Axes object, optional, default: None
        Parent axes of the plot. It uses gca() if not specified.
    vmin, vmax : scalar, optional, default: None
        `vmin` and `vmax` are used in conjunction with `norm` to normalize
        luminance data.  If either are `None`, the min and max of the
        color array is used.  (Note if you pass a `norm` instance, your
        settings for `vmin` and `vmax` will be ignored.)

    Returns
    -------
    paths : `~matplotlib.collections.PathCollection`

    Other parameters
    ----------------
    kwargs : `~matplotlib.collections.Collection` properties
        eg. alpha, edgecolors, facecolors, linewidths, linestyles, norm, cmap

    Examples
    --------
    a = np.arange(11)
    circles(a, a, a*0.2, c=a, alpha=0.5, edgecolor='none')

    License
    --------
    This code is under [The BSD 3-Clause License]
    (http://opensource.org/licenses/BSD-3-Clause)
    """
    from matplotlib.patches import Circle
    from matplotlib.collections import PatchCollection
    import pylab as plt
    #import matplotlib.colors as colors

    if ax is None:
        ax = plt.gca()    

    if isinstance(c,basestring):
        color = c     # ie. use colors.colorConverter.to_rgba_array(c)
    else:
        color = None  # use cmap, norm after collection is created
    kwargs.update(color=color)

    if np.isscalar(x):
        patches = [Circle((x, y), s),]
    elif np.isscalar(s):
        patches = [Circle((x_,y_), s) for x_,y_ in zip(x,y)]
    else:
        patches = [Circle((x_,y_), s_) for x_,y_,s_ in zip(x,y,s)]
    collection = PatchCollection(patches, **kwargs)

    if color is None:
        collection.set_array(np.asarray(c))
        if vmin is not None or vmax is not None:
            collection.set_clim(vmin, vmax)

    ax.add_collection(collection)
    return collection

def colorMsg(color):
    print("Available color schemes (name: resmin -- resmax)")
    for i in color.info():
        print("%s: %d -- %d" % (i["name"], i["low"], i["high"]))

def ag_to_svg(circles, colors, tresh=0.005):
    """
    Convert a list of circles to svg, optionally color them.
    @param circles: A list of L{Circle}s
    @param colors: A L{ColorMap} object
    @param tresh: Only circles with a radius greater than the product of tresh and maximal radius are saved
    """
    svg = []
    
    # Find the biggest circle, which hopefully is the enclosing one
    # and has a negative radius because of this. Note that this does
    # not have to be the case if we picked an unlucky set of radii at
    # the start. If that was the case, we're screwed now.
    
    big = min(circles, key=lambda c: c.r.real)

    # Move biggest circle to front so it gets drawn first
    circles.remove(big)
    circles.insert(0, big)

    if big.r.real < 0:
        # Bounding box from biggest circle, lower left corner and two
        # times the radius as width
        corner = big.m - ( abs(big.r) + abs(big.r) * 1j )
        vbwidth = abs(big.r)*2
        width = 500 # Hardcoded!

        # Line width independent of circle size
        lw = (vbwidth/width)

        svg.append('<svg xmlns="http://www.w3.org/2000/svg" width="%f" height="%f" viewBox="%f %f %f %f">\n' % (width, width, corner.real, corner.imag, vbwidth, vbwidth))
        # plt.
        # Keep stroke width relative
        svg.append('<g stroke-width="%f">\n' % lw)

        # Iterate through circle list, circles with radius<radmin
        # will not be saved because they are too small for printing.
        radmin = tresh * abs(big.r)
        # fig=plt.gcf()
        # fig.set_size_inches(20,20)

        # fig.
        for c in circles:
            if abs(c.r) > radmin:
                fill = colors.color_for(abs(c.r))
    #             # circle=plt.Circle((c.m.real, c.m.imag), abs(c.r),color='r')#,color=fill)#,fill=False)#,color='r')
    #             # fig.gca().add_artist(circle)
                svg.append(( '<circle cx="%f" cy="%f" r="%f" fill="%s" stroke="black"/>\n' % (c.m.real, c.m.imag, abs(c.r), fill)))
    #             # circles_C(c.m.real, c.m.imag, abs(c.r))
        svg.append('</g>\n')
        svg.append('</svg>\n')
    # # plt.show()
    # return ''.join(svg)
    return circles,radmin,big,''.join(svg)

def impossible_combination(c1, c2, c3):
    # If any curvatures x, y, z satisfy the equation
    # x = 2*sqrt(y*z) + y + z
    # then no fourth enclosing circle can be genereated, because it
    # would be a line.
    # We need to see for c1, c2, c3 if they could be "x".
    
    impossible = False
    
    sets = [(c1,c2,c3), (c2,c3,c1), (c3,c1,c2)]
    
    for (x, y, z) in sets:
        if x == 2*math.sqrt(y*z) + y + z:
            impossible = True
    
    return impossible

# def main():
color = ColorScheme("colorbrewer.json")
available = [d['name'] for d in color.info()]
# fig=plt.gcf()
# args = parseArguments(sys.argv, available)
cc_list=[[2., 2., 2.]]
# Sanity checks
depth=5
treshold=0.005
width = 500
fig,ax=plt.subplots(figsize=(50,50))
# fig, ax = plt.subplots(1)
for en,ccc in enumerate(cc_list):
    # print en,ccc
    for c in ccc:
        if c == 0:
            print("Error: curvature or radius can't be 0")
            exit(1)
        if impossible_combination(ccc[0],ccc[1],ccc[2]):
            print("Error: no apollonian gasket possible for these curvatures")
            exit(1)

        # Given curvatures were in fact radii, so take the reciprocal
        # if args.radii:

        # c1 = 1/ccc[0]
        # c2 = 1/ccc[1]
        # c3 = 1/ccc[2]
        c1=ccc[0]
        c2=ccc[1]
        c3=ccc[2]

        ag = ApollonianGasket(c1,c2,c3)

        # At a recursion depth > 10 things start to get serious.
        # if args.depth > 10:
        #     if not args.force:
        #         print("Note: Number of cicles increases exponentially with 2*3^{D+1} at depth D.\nIf you want to use D>10, specify the --force option.")
        #         args.depth = 10

        ag.generate(depth)

        # Get smallest and biggest radius
        smallest = abs(min(ag.genCircles, key=lambda c: abs(c.r.real)).r.real)
        biggest = abs(max(ag.genCircles, key=lambda c: abs(c.r.real)).r.real)

        # Construct color map 
        # if args.color == 'none':
        mp = ColorMap('none')
        # else:
        #     # TODO: resolution of 8 is hardcoded, some color schemes have
        #     # resolutions up to 11. Make this configurable.
        # mp = color.makeMap(smallest, biggest, args.color, 8)
        # plt.figure(figsize=(18,18))
        # ax=plt.subplot(aspect='equal')
        # fig,ax=
        stitl='Apollonian Circles (for iterations = %i) \nwith curvatures (%i, %i, %i)' %(depth, c1,c2,c3)
        plt.subplot(1,1,1).set_title(stitl, fontsize=18)#,aspect='equal')
        

        # ax.aspect('equal')
        # fig, ax = plt.subplots(1)
        # svg = ag_to_svg(ag.genCircles, mp, tresh=treshold)
        circles ,radmin,big,svg= ag_to_svg(ag.genCircles, mp, tresh=treshold)
        # radmin = tresh * abs(big.r)
        aa=[]
        bb=[]
        cen=[]
        # plt.subplot(2,3,5)
        for circ in circles:
            # print circ,radmin
            if abs(circ.r) > radmin:
                fill = mp.color_for(abs(circ.r))
                # print fill
                # aa.append(circ.m.real)
                # bb.append(circ.m.imag)
                # cen.append(abs(circ.r))
                aa=(random.random(),random.random(),random.random())
                circles_C(circ.m.real, circ.m.imag, abs(circ.r),c=aa,alpha=0.2)
        # circles_C(aa,bb,cen,c=x,ax=ax,alpha=0.2)
        plt.axis('equal')
        plt.axis('off')
plt.show()
        # User supplied filename? If not, we need to construct something.
        # if len(args.output) == 0:
        # output = 'agS_%.4f_%.4f_%.4f.svg' % (c1, c2, c3)

        # with open(output, 'w') as f:
        #     f.write(svg)
        #     f.close()

        # if( __name__ == "__main__" ):
            # main()
