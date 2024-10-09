import random

class Dados:
    def __init__(self, cantidad=1):
        """
        Inicializa la clase Dados con la cantidad de dados a tirar.
        Por defecto, se tira 1 dado.
        """
        self.cantidad = cantidad

    def tirar(self):
        """
        Simula tirar los dados y retorna una lista con los resultados.
        Cada dado tiene un valor entre 1 y 6.
        """
        resultados = [random.randint(1, 6) for _ in range(self.cantidad)]
        return resultados
