from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

pacientes = []

class Paciente(Resource):
    def get(self, ci=None):
        if ci:
            for paciente in pacientes:
                if paciente['CI'] == ci:
                    return jsonify(paciente)
            return {'error': 'Paciente no encontrado'}, 404
        else:
            return jsonify(pacientes)

    def post(self):
        nuevo_paciente = request.get_json()
        pacientes.append(nuevo_paciente)
        return nuevo_paciente, 201

    def put(self, ci):
        for paciente in pacientes:
            if paciente['CI'] == ci:
                paciente.update(request.get_json())
                return paciente, 200
        return {'error': 'Paciente no encontrado'}, 404

    def delete(self, ci):
        global pacientes
        pacientes = [paciente for paciente in pacientes if paciente['CI'] != ci]
        return {'message': 'Paciente eliminado'}, 200

api.add_resource(Paciente, '/pacientes', '/pacientes/<string:ci>')

if __name__ == '__main__':
    app.run(debug=True)
