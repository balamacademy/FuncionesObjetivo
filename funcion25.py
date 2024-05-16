import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def townsend_modified(x, y):
    return -(np.cos((x - 0.1) * y))**2 - x * np.sin(3 * x + y)

def constraint(x, y):
    t = np.arctan2(x, y)
    return (x**2 + y**2) - ((2 * np.cos(t) - 0.5 * np.cos(2 * t) - 0.25 * np.cos(3 * t) - 0.125 * np.cos(4 * t))**2 + (2 * np.sin(t))**2)

def plot_townsend_modified_constraint():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z_townsend = townsend_modified(X, Y)
    Z_constraint = constraint(X, Y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, Z_townsend, cmap='viridis', alpha=0.7)
    ax.plot_surface(X, Y, Z_constraint, color='red', alpha=0.2)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Townsend Modified Function Constrained")

    plt.show()


plot_townsend_modified_constraint()