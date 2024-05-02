import numpy as np
import matplotlib.pyplot as plt


def matyas_function(x,y):
    operacion = 0.26 * (x**2 + y**2) - 0.48 * x * y 
    return operacion


def plot_matyas_function():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-10,10, 100)
    y = np.linspace(-10,10, 100)
    x, y = np.meshgrid(x, y)
    z = matyas_function(x, y)

    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Bukin Function N.6')
    plt.title('Bukin Function N.6')

    plt.show()

plot_matyas_function()
