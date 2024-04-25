import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def goldstein_price_function(x, y):
    part1 = 1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)
    part2 = 30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2)
    return part1 * part2

def plot_goldstein_price_function():
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    x, y = np.meshgrid(x, y)
    z = goldstein_price_function(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
    ax.set_title('Goldstein-Price Function')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

# Ejemplo de uso
plot_goldstein_price_function()
