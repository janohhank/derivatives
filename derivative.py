import math
import numpy
import matplotlib.pyplot
import scipy.interpolate

# domain
df = numpy.arange(-2.0,2.1,0.1)

# original function:
# f(x) = -x * sin(x^2) + 42
rf = []

# first derivative:
# f'(x) = -2 * x^2 * cos(x^2) - sin(x^2)
rf_dx = []
rf_dx_degree = []   # arctangent of dx/dy

# second derivative:
# f''(x) = 2 * x (2 * x^2 * sin(x^2) - 3 * cos(x^2)
rf_ddx = []
rf_ddx_degree = []  # arctangent of dx/dy

# calculate values
for x in df:
    # original
	rf.append(-x * math.sin(x**2) + 42)

    # first derivative
	dx = -2 * x**2 * math.cos(x**2) - math.sin(x**2)
	rf_dx.append(dx)
	rf_dx_degree.append(math.atan(dx) * 180 / math.pi)

    # second derivative
	ddx = 2 * x * (2 * x**2 * math.sin(x**2) - 3 * math.cos(x**2))
	rf_ddx.append(ddx)
	rf_ddx_degree.append(math.atan(ddx) * 180 / math.pi)

# calculate values for the arrow vectors
length = 0.5
dx_arrow_end_x = []
dx_arrow_end_y = []
ddx_arrow_end_x = []
ddx_arrow_end_y = []
for i in range(df.size):
	dx_arrow_end_x.append(df[i] + length * math.cos(math.radians(rf_dx_degree[i])))
	dx_arrow_end_y.append(rf[i] + length * math.sin(math.radians(rf_dx_degree[i])))
	
	ddx_arrow_end_x.append(df[i] + length * math.cos(math.radians(rf_ddx_degree[i])))
	ddx_arrow_end_y.append(rf_dx[i] + length * math.sin(math.radians(rf_ddx_degree[i])))

# coloring arrows based on degrees
norm_dx = matplotlib.colors.Normalize(vmin=min(rf_dx_degree), vmax=max(rf_dx_degree), clip=True)
mapper_dx = matplotlib.cm.ScalarMappable(norm=norm_dx, cmap=matplotlib.cm.RdYlGn)

norm_ddx = matplotlib.colors.Normalize(vmin=min(rf_ddx_degree), vmax=max(rf_ddx_degree), clip=True)
mapper_ddx = matplotlib.cm.ScalarMappable(norm=norm_ddx, cmap=matplotlib.cm.RdYlGn)

# plot functions and derivatives
fig, ((ax1, ax2), (ax3, ax4)) = matplotlib.pyplot.subplots(2, 2)
fig.suptitle('Visualization Of Derivatives', fontweight='bold')

df_linspace = numpy.linspace(df.min(), df.max(), 500)
fx_spline = scipy.interpolate.make_interp_spline(df, rf)
ax1.plot(df_linspace, fx_spline(df_linspace))
ax1.set_title('f(x)', fontweight='bold')

ax2.plot()
ax2.set_title('d/dx [f(x)]', fontweight='bold')
for i in range(df.size):
	ax2.arrow(df[i], rf[i], dx_arrow_end_x[i] - df[i], dx_arrow_end_y[i] - rf[i], width=0.009, color=mapper_dx.to_rgba(rf_dx_degree[i]))

fx_dx_spline = scipy.interpolate.make_interp_spline(df, rf_dx)
ax3.plot(df_linspace, fx_dx_spline(df_linspace))
ax3.set_title('d/dx [f(x)]', fontweight='bold')

ax4.plot()
ax4.set_title('$d^2$/d$x^2$ [f(x)]', fontweight='bold')
for i in range(df.size):
	ax4.arrow(df[i], rf_dx[i], ddx_arrow_end_x[i] - df[i], ddx_arrow_end_y[i] - rf_dx[i], width=0.009, color=mapper_ddx.to_rgba(rf_ddx_degree[i]))

matplotlib.pyplot.show()
