import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mishras_bird(x, y):
    return np.sin(y) * np.exp((1 - np.cos(x))**2) + np.cos(x) * np.exp((1 - np.sin(y))**2) + (x - y)**2

def constraint(x, y):
    return (x + 5)**2 + (y + 5)**2 - 25


def plot_mishras_bird_constrait():
    x = np.linspace(-10, 0, 100)
    y = np.linspace(-10, 0, 100)
    X, Y = np.meshgrid(x, y)
    Z_mishras_bird = mishras_bird(X, Y)
    Z_constraint = constraint(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, Z_mishras_bird, cmap='viridis', alpha=0.7)
    ax.plot_surface(X, Y, Z_constraint, color='red', alpha=0.2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Mishra's Bird Function Constrained")
    plt.show()



plot_mishras_bird_constrait()