import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(7,5))
fig.patch.set_facecolor('cyan')
ax = plt.subplot(111)#,axisbg='b')
# ax.set_axis_bgcolor('b')
########################################
## c parameter for plot : change this ##
########################################

c = np.complex(-1,0)
#c = np.complex(-0.9,0)
#c = np.complex(0.279,0)

plt.suptitle('Juila Set with c = -1 (1000 iterations)', fontsize=16);
########################################

#########################################################
## Size of side grid for J_c plot: change for accuracy ##
#########################################################
grid = 500;   #500
#########################################################

#############################################################
## number of iterations we use to test for escape : change ##
#############################################################
escape = 1000  #2000
#############################################################

absc = np.abs(c);
rc = 0.5+np.sqrt(0.25+absc);

#####################################
## Region of plot: change for zoom ##
#####################################

xmin = -2.279
xmax = +2.279
ymin = -2.279
ymax = +2.279

# xmin = -2.0
# xmax = +2.0
# ymin = -2.0
# ymax = +2.0

#xmin = 0.0
#xmax = 1.0
#ymin = 0.0
#ymax = 1.0
#xmin = 0.5
#xmax = 0.7
#ymin = 0
#ymax = 0.2
#xmin = 0.6
#xmax = 0.65
#ymin = 0
#ymax = 0.05
#xmin = 0.618
#xmax = 0.619
#ymin = 0
#ymax = 0.001
######################################

x_range = np.arange(xmin, xmax, (xmax - xmin) / grid);
y_range = np.arange(ymin, ymax, (ymax - ymin) / grid);

plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
pointSize = (xmax- xmin)/grid;

# Generate keep set points
print "Running ... "
for y in y_range:
    for x in x_range:
        z = np.complex(x, y)
        escapecount=0

        #  tests if z is in the keep set (i.e. filled in Julia Set)
        while np.abs(z) <= rc and escapecount < escape:
            z = z*z + c;
            escapecount+=1;
            
        # Write point to plot if we have tried to get out escape times and failed
        if escapecount == escape :
            keepSetPoint = plt.Circle((x,y), radius=pointSize, color='r');
            ax.add_patch(keepSetPoint);   

plt.axis("off")    
plt.show()