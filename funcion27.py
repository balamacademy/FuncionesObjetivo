import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def simionescu(x, y):
    return 0.1 * x * y

def constraint(x, y):
    r_T = 1
    r_S = 0.2
    n = 8
    return (x**2 + y**2) - (r_T + r_S * np.cos(n * np.arctan2(x, y)))**2



x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z_simionescu = simionescu(X, Y)
Z_constraint = constraint(X, Y)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z_simionescu, cmap='viridis', alpha=0.7)
ax.plot_surface(X, Y, Z_constraint, color='red', alpha=0.2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Simionescu Function Constrained")
plt.show()
