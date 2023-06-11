import matplotlib.pyplot as plt
import numpy as np

def mostrarGrafico():
    x = np.arange(-100, 100)
    plt.plot(x, 3.33 - 0.33 * x, label = 'x + 3y <= 10')
    plt.plot(x, 12.5 - 0.25 * x, label = 'x + 4y <= 50')

    plt.axis([0, 50, 0, 13])
    plt.grid(True)
    plt.legend
    plt.show()

def mostrarGraficoResultado():
    x = np.arange(-100, 100)
    plt.plot(x, 3.33 - 0.33 * x, label = 'x + 3y <= 10')
    plt.plot(x, 12.5 - 0.25 * x, label = 'x + 4y <= 50')

    x = [10, 0, 0, 0]
    y = [0, 0, 0, 3.33]

    plt.fill(x, y, 'grey')

    plt.axis([0, 50, 0, 13])
    plt.grid(True)
    plt.legend
    plt.show()