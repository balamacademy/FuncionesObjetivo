import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mccormick(x, y):
    return np.sin(x + y) + (x - y)**2 - 1.5*x + 2.5*y + 1

def plot_maccormick():
    x = np.linspace(-3, 4, 100)
    y = np.linspace(-3, 4, 100)
    X, Y = np.meshgrid(x, y)
    Z = mccormick(X, Y)


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('McCormick(X, Y)')
    ax.set_title('Función de McCormick')


    plt.show()


plot_maccormick()
