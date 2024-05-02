import numpy as np
import matplotlib.pyplot as plt

def rosenbrock_function(x, y, a=1, b=100):
    return (a - x) ** 2 + b * (y - x ** 2) ** 2

def plot_rosenbrock_function():
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-1, 3, 400)
    x, y = np.meshgrid(x, y)
    z = rosenbrock_function(x, y)
    fig, ax = plt.subplots()
    CS = ax.contour(x, y, z, np.logspace(-0.5, 3.5, 20, base=10), cmap='viridis')
    ax.plot(1, 1, 'r*', markersize=10)  # Mínimo global
    ax.set_title('Rosenbrock Function')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.colorbar(CS)
    plt.show()


plot_rosenbrock_function()
