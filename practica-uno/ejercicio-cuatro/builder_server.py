class PacienteBuilder:
    def __init__(self):
        self.paciente = {}

    def con_ci(self, ci):
        self.paciente['ci'] = ci
        return self

    def con_nombre(self, nombre):
        self.paciente['nombre'] = nombre
        return self

    def con_apellido(self, apellido):
        self.paciente['apellido'] = apellido
        return self

    def con_edad(self, edad):
        self.paciente['edad'] = edad
        return self

    def con_genero(self, genero):
        self.paciente['genero'] = genero
        return self

    def con_diagnostico(self, diagnostico):
        self.paciente['diagnostico'] = diagnostico
        return self

    def con_doctor(self, doctor):
        self.paciente['doctor'] = doctor
        return self

    def construir(self):
        return self.paciente
