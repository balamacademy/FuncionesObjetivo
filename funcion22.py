import numpy as np
import matplotlib.pyplot as plt



def rosenbrock(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2

def constraint1(x, y):
    return (x - 1)**3 - y + 1

def constraint2(x, y):
    return x + y - 2



x = np.linspace(-1, 2, 400)
y = np.linspace(-1, 3, 400)
X, Y = np.meshgrid(x, y)
Z_rosenbrock = rosenbrock(X, Y)
Z_constraint1 = constraint1(X, Y)
Z_constraint2 = constraint2(X, Y)



plt.contour(X, Y, Z_rosenbrock, levels=np.logspace(-1, 3, 10), cmap='viridis', alpha=0.7)
plt.colorbar(label='Rosenbrock')


plt.contour(X, Y, Z_constraint1, levels=[0], colors='red', linestyles='solid')
plt.contour(X, Y, Z_constraint2, levels=[0], colors='blue', linestyles='solid')


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Rosenbrock Function with Constraints')


plt.grid(True)
plt.show()
