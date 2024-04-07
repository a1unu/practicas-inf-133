import random

class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("Esta clase es un singleton!")
        else:
            Singleton._instance = self
            self.partidas = []

    def jugar(self, elemento_jugador):
        elementos = ['piedra', 'papel', 'tijera']
        elemento_servidor = random.choice(elementos)
        if elemento_jugador == elemento_servidor:
            resultado = 'empató'
        elif (elemento_jugador == 'piedra' and elemento_servidor == 'tijera') or (elemento_jugador == 'papel' and elemento_servidor == 'piedra') or (elemento_jugador == 'tijera' and elemento_servidor == 'papel'):
            resultado = 'ganó'
        else:
            resultado = 'perdió'
        partida = {'id': len(self.partidas) + 1, 'elemento': elemento_jugador, 'elemento_servidor': elemento_servidor, 'resultado': resultado}
        self.partidas.append(partida)
        return partida
