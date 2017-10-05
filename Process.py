import numpy as np
import matplotlib.pyplot as plt

class Process(object):
    
    def __init__(self, data):
        self.data = data

    def plotSetosa(self):
        # Exibindo o comprimento da sépala da iris setosa
        plt.plot(self.data[:50, 0], 'r-', marker = 'o', ms = 6, label = 'Comp. Sépala Iris-Setosa')
        plt.show()

    def plotVscolor(self):
        # Exibindo o comprimento da sépala da iris Versicolour
        plt.plot(self.data[50: 100, 0], 'g--', marker = 'o', ms = 6, label = 'Comp. Sépala Iris-Versicolour')
        plt.show()
    
    def plotCompSetVs(self):
        plt.plot(self.data[:50, 0], c ='Black', ls = '-', marker = 's', ms = 6, label = 'Comp. Sépala Iris-Setosa')
        plt.plot(self.data[50: 100, 0], 'r-', marker = 'o', ms = 6, label = 'Comp. Sépala Iris-Versicolour')
        plt.legend()
        plt.show()