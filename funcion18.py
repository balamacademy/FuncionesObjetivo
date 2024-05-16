import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def schaffer_function_n2(x, y):
    return 0.5 + ((np.sin(x**2 - y**2)**2 - 0.5) / (1 + 0.001*(x**2 + y**2))**2)


def plot_schaffer_funtion_n2():
    x = np.linspace(-50, 50, 100)
    y = np.linspace(-50, 50, 100)
    X, Y = np.meshgrid(x, y)
    Z = schaffer_function_n2(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Schaffer N. 2(X, Y)')
    ax.set_title('Función Schaffer N. 2')


    plt.show()


plot_schaffer_funtion_n2()
