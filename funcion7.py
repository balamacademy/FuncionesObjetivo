import numpy as np
import matplotlib.pyplot as plt


def booth_function(x,y):
    operacion = ((x + 2*y - 7)**2) + ((2*x + y - 5)**2)
    return operacion


def booth_function_plot():
    fig = plt.figure()
    ax = fig.add_subplot()
    x = np.linspace(-10, 10, 3)
    y = np.linspace(-10, 10, 3)
    x, y = np.meshgrid(x, y)
    z = booth_function(x,y)
    z = z.reshape(x.shape)
    ax.contourf(x, y, z, cmap='viridis')
    punto_inicial = (1,3)
    ax.scatter(punto_inicial[0], punto_inicial[1], color='red', label='Punto Inicial')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Sphere Function')
    plt.legend()
    plt.show()
booth_function_plot()


