import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




def ackley_funtion(x, y):
    return -20*np.exp(-0.2*np.sqrt(0.5*(x**2 + y**2))) - np.exp(0.5*(np.cos(2*np.pi*x) + np.cos(2*np.pi*y))) + np.e + 20



def plot_ackley_funtion():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)

    x, y = np.meshgrid(x, y)
    
    z = ackley_funtion(x, y)
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
    fig.colorbar(surf)
    ax.set_title('Función de Ackley')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('f(X, Y)')
    plt.show()






plot_ackley_funtion()

