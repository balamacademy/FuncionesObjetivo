import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def beale_function(x, y):
    return (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2

def plot_beale_function():
    x = np.linspace(-4.5, 4.5, 400)
    y = np.linspace(-4.5, 4.5, 400)
    x, y = np.meshgrid(x, y)
    z = beale_function(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
    ax.set_title('Beale Function')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

# Ejemplo de uso
plot_beale_function()
