import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

def styblinski_tang_2d(x, y):
    return (x**4 - 16*x**2 + 5*x + y**4 - 16*y**2 + 5*y) / 2


def plot_styblinski_tang_2d():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = styblinski_tang_2d(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Styblinski-Tang(X, Y)')
    ax.set_title('Función Styblinski-Tang (2D)')

    plt.show()


plot_styblinski_tang_2d()