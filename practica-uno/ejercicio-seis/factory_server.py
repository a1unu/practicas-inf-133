class AnimalFactory:
    def crear_animal(self, tipo):
        if tipo == 'Mamífero':
            return Mamifero()
        elif tipo == 'Ave':
            return Ave()
        elif tipo == 'Reptil':
            return Reptil()
        elif tipo == 'Anfibio':
            return Anfibio()
        elif tipo == 'Pez':
            return Pez()
        else:
            raise ValueError("Tipo de animal no válido")

class Mamifero:
    def __init__(self):
        self.tipo = 'Mamífero'
        self.caracteristicas = 'Tiene pelo y amamanta a sus crías'

class Ave:
    def __init__(self):
        self.tipo = 'Ave'
        self.caracteristicas = 'Tiene plumas y pone huevos'

class Reptil:
    def __init__(self):
        self.tipo = 'Reptil'
        self.caracteristicas = 'Tiene escamas y es de sangre fría'

class Anfibio:
    def __init__(self):
        self.tipo = 'Anfibio'
        self.caracteristicas = 'Vive tanto en agua como en tierra'

class Pez:
    def __init__(self):
        self.tipo = 'Pez'
        self.caracteristicas = 'Vive en el agua y tiene aletas'
