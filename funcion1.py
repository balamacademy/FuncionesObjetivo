# N dimensionnes = 3
# punto inicial = [-2,-2,-2]

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# def rastrigin_function(x):
#     A = 10
#     return A * len(x) + sum([(xi**2 - A * np.cos(2 * np.pi * xi)) for xi in x])
# def plot_rastrigin_function():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     x = np.linspace(-5.12, 5.12, 100)
#     y = np.linspace(-5.12, 5.12, 100)
#     x, y = np.meshgrid(x, y)
#     z = rastrigin_function([x, y])
#     ax.plot_surface(x, y, z, cmap='viridis')
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Rastrigin Function')
#     plt.title('Rastrigin Function')
#     plt.show()
# plot_rastrigin_function()












import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rastrigin_function(x):
    A = 10
    return A * len(x) + sum([(xi**2 - A * np.cos(2 * np.pi * xi)) for xi in x])

def plot_rastrigin_function():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(-5.12, 5.12, 100)
    y = np.linspace(-5.12, 5.12, 100)
    x, y = np.meshgrid(x, y)
    z = rastrigin_function([x, y])
    ax.plot_surface(x, y, z, cmap='viridis')
    punto_inicial = [-2, -2, -2]
    ax.scatter(punto_inicial[0], punto_inicial[1], rastrigin_function(punto_inicial), color='red', label='Punto Inicial')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Rastrigin Function')
    plt.title('Rastrigin Function')
    plt.legend()
    plt.show()
plot_rastrigin_function()


