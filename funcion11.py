import numpy as np
import matplotlib.pyplot as plt


def himmelblaus(x,y):
    operacion = ((x**2 + y - 11)**2) + ((x + y**2 - 7)**2)
    return operacion


def himmelblaus_plot():
    fig = plt.figure()
    ax = fig.add_subplot()
    x = np.linspace(-5.1, 5.1, 100)
    y = np.linspace(-5.1, 5.1, 100)
    x, y = np.meshgrid(x, y)
    z = himmelblaus(x,y)
    z = z.reshape(x.shape)
    ax.contourf(x, y, z, cmap='viridis')
    punto_inicial = (0,0)
    ax.scatter(punto_inicial[0], punto_inicial[1], color='red', label='Punto Inicial')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Sphere Function')
    plt.legend()
    plt.show()
himmelblaus_plot()




















