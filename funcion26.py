import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gomez_and_levy_modified(x, y):
    return 4*x**2 - 2.1*x**4 + (1/3)*x**6 + x*y - 4*y**2 + 4*y**4

def constraint(x, y):
    return -np.sin(4*np.pi*x) + 2*np.sin(2*np.pi*y)**2 - 1.5

def plot_gomez_and_levy_modified_constraint():
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z_gomez_and_levy = gomez_and_levy_modified(X, Y)
    Z_constraint = constraint(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z_gomez_and_levy, cmap='viridis', alpha=0.7)
    ax.plot_surface(X, Y, Z_constraint, color='red', alpha=0.2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Gómez and Levy Modified Function Constrained")
    plt.show()


plot_gomez_and_levy_modified_constraint()