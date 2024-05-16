import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rosenbrock(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2


def disk_constraint(x, y):
    return x**2 + y**2 

def plot_rosenbrock_constraint_disk():
    x = np.linspace(-1.5, 1.5, 100)
    y = np.linspace(-1.5, 1.5, 100)
    X, Y = np.meshgrid(x, y)
    Z_rosenbrock = rosenbrock(X, Y)
    Z_constraint = disk_constraint(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, Z_rosenbrock, cmap='viridis', alpha=0.7)

    ax.plot_surface(X, Y, Z_constraint, color='red', alpha=0.2)
    
    ax.scatter(1.0, 1.0, 0, color='black', marker='o', s=100)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Función de Rosenbrock con restricción')
    plt.show()


plot_rosenbrock_constraint_disk()


