import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def threehump_camel_function(x, y):
    return 2*x**2 - 1.05*x**4 + (x**6)/6 + x*y + y**2

def plot_threehump_camel_function():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-5.1, 5.1, 100)
    y = np.linspace(-5.1, 5.1, 100)
    x, y = np.meshgrid(x, y)
    z = threehump_camel_function(x, y)

    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Three-Hump Camel Function')
    plt.title('Three-Hump Camel Function')

    plt.show()

plot_threehump_camel_function()



# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# def threehump_camel_function(x, y):
#     return 2*x**2 - 1.05*x**4 + (x**6)/6 + x*y + y**2

# def plot_threehump_camel_function():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     x = np.linspace(-5.1, 5.1, 100)
#     y = np.linspace(-5.1, 5.1, 100)
#     x, y = np.meshgrid(x, y)
#     z = threehump_camel_function(x, y)
#     ax.plot_surface(x, y, z, cmap='viridis')
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Three-Hump Camel Function')
#     plt.title('Three-Hump Camel Function')
#     plt.show()
# plot_threehump_camel_function()
