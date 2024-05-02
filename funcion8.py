import numpy as np
import matplotlib.pyplot as plt


def bukin_function(x,y):
    operacion = 100*(np.sqrt(np.abs(y - 0.01 * x**2))) + 0.01 * np.abs(x + 10)
    return operacion


def plot_bukin_function():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-15, -5, 100)
    y = np.linspace(-3, 3, 100)
    x, y = np.meshgrid(x, y)
    z = bukin_function(x, y)

    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Bukin Function N.6')
    plt.title('Bukin Function N.6')

    plt.show()

plot_bukin_function()

