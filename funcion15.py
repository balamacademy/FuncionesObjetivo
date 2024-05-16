import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def eggholder(x, y):
    return (-(y + 47) * np.sin(np.sqrt(abs(x/2 + (y + 47)))) - x * np.sin(np.sqrt(abs(x - (y + 47)))))


def plot_eggholder():
    x = np.linspace(-512, 512, 100)
    y = np.linspace(-512, 512, 100)
    X, Y = np.meshgrid(x, y)
    Z = eggholder(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Eggholder(X, Y)')
    ax.set_title('Función Eggholder')

    plt.show()


plot_eggholder()
