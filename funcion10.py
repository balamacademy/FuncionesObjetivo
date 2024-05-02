import numpy as np
import matplotlib.pyplot as plt


def levi_function(x, y):
    return np.sin(3*np.pi*x)**2 + (x-1)**2 * (1 + np.sin(3*np.pi*y)**2) + (y-1)**2 * (1 + np.sin(2*np.pi*y)**2)



def plot_levi_function():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-10,10, 100)
    y = np.linspace(-10,10, 100)
    x, y = np.meshgrid(x, y)
    z = levi_function(x, y)

    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Lévi function N.13')
    plt.title('Lévi function N.13')

    plt.show()

plot_levi_function()
