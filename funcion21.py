import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def shekel_function(x, y, C, beta):
    sum = 0
    for i in range(len(C)):
        sum += 1.0 / (np.dot(np.array([x, y]) - C[i], np.array([x, y]) - C[i]) + beta[i])
    return -sum


def plot_shekel():
    C = [np.array([1, 2]), np.array([-1, -1]), np.array([2, -2])]
    beta = [0.1, 0.2, 0.2]

    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    x, y = np.meshgrid(x, y)
    z = np.array([shekel_function(x_, y_, C, beta) for x_, y_ in zip(np.ravel(x), np.ravel(y))])
    z = z.reshape(x.shape)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
    ax.set_title('Shekel Function (Simplified)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


plot_shekel()