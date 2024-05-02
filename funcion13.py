import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def easom_function(x, y):
    return -np.cos(x) * np.cos(y) * np.exp(-((x - np.pi)**2 + (y - np.pi)**2))

def plot_easom_function():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-100, 100, 100)
    y = np.linspace(-100, 100, 100)
    x, y = np.meshgrid(x, y)
    z = easom_function(x, y)

    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Easom Function')
    plt.title('Easom Function')

    plt.show()

plot_easom_function()
