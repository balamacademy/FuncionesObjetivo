# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# def sphere_function(x):
#     return sum([xi**2 for xi in x])

# def plot_sphere_function():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     x = np.linspace(-5.1, 5.1, 100)
#     y = np.linspace(-5.1, 5.1, 100)
#     x, y = np.meshgrid(x, y)
#     z = np.array([sphere_function([x_i, y_i]) for x_i, y_i in zip(np.ravel(x), np.ravel(y))])
#     z = z.reshape(x.shape)
#     ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Sphere Function')
#     ax.set_title('Sphere Function')
#     plt.show()
# plot_sphere_function()










import numpy as np
import matplotlib.pyplot as plt

def sphere_function(x):
    return sum([xi**2 for xi in x])

def plot_sphere_function():
    fig = plt.figure()
    ax = fig.add_subplot()
    x = np.linspace(-5.1, 5.1, 100)
    y = np.linspace(-5.1, 5.1, 100)
    x, y = np.meshgrid(x, y)
    z = np.array([sphere_function([x_i, y_i]) for x_i, y_i in zip(np.ravel(x), np.ravel(y))])
    z = z.reshape(x.shape)
    ax.contourf(x, y, z, cmap='viridis')
    punto_inicial = (-1, 1.5)
    ax.scatter(punto_inicial[0], punto_inicial[1], color='red', label='Punto Inicial')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Sphere Function')
    plt.legend()
    plt.show()
plot_sphere_function()

