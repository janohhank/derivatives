import math
import numpy
import matplotlib.pyplot
import scipy.interpolate

# domain
df = numpy.arange(-5.0,5.0,0.1)

# original function:
# f(x,y) = x^2 + y^2
rf = []

# partial derivatives
# d/dx = 2x
rf_dx = []
rf_dx_degree = []
# d/dy = 2y
rf_dy = []
rf_dy_degree = []

# calculate values
for x in df:
    rf_partial_result = []
    rf_dx_partial_result = []
    rf_dy_partial_result = []
    for y in df:
        rf_partial_result.append(x**2 + y**2)

        rf_dx_partial_result.append(2 * x)
        rf_dy_partial_result.append(2 * y)
    rf.append(rf_partial_result)
    rf_dx.append(rf_dx_partial_result)
    rf_dy.append(rf_dy_partial_result)

X, Y = numpy.meshgrid(df, df)

# plot partial derivatives and gradient vector
fig = matplotlib.pyplot.figure()
fig.suptitle('Visualization Of Partial Derivatives', fontweight='bold')

ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.plot_surface(X, Y, numpy.array(rf), cmap='terrain')
ax1.set_title('f(x,y)', fontweight='bold')

ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.plot_surface(X, Y, numpy.array(rf_dx), cmap='terrain')
ax2.set_title('d/dx [f(x,y)]', fontweight='bold')

ax3 = fig.add_subplot(2, 2, 3, projection='3d')
ax3.plot_surface(X, Y, numpy.array(rf_dy), cmap='terrain')
ax3.set_title('d/dy [f(x,y)]', fontweight='bold')

ax4 = fig.add_subplot(2, 2, 4)
ax4.contourf(X, Y, numpy.array(rf), cmap='terrain')
ax4.set_title(''r'$\nabla \partial$', fontweight='bold')

for x in range(df.size):
    for y in range(df.size):
        if (x % 5 == 0 and y % 5 == 0):
            ax4.arrow(
                df[x],
                df[y],
                0.05 * (df[x] - rf_dx[x][y]),
                0.05 * (df[y] - rf_dy[x][y]),
                width=0.03)

matplotlib.pyplot.show()
