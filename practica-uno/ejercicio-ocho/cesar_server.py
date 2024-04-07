from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

mensajes = []

def cifrado_cesar(texto):
    resultado = ""
    for char in texto:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - ascii_offset + 3) % 26 + ascii_offset)
        else:
            resultado += char
    return resultado

class Mensaje(Resource):
    def get(self, id=None):
        if id:
            for mensaje in mensajes:
                if mensaje['ID'] == id:
                    return jsonify(mensaje)
            return {'error': 'Mensaje no encontrado'}, 404
        else:
            return jsonify(mensajes)

    def post(self):
        nuevo_mensaje = request.get_json()
        nuevo_mensaje['Contenido encriptado'] = cifrado_cesar(nuevo_mensaje['Contenido'])
        mensajes.append(nuevo_mensaje)
        return nuevo_mensaje, 201

    def put(self, id):
        for mensaje in mensajes:
            if mensaje['ID'] == id:
                mensaje.update(request.get_json())
                mensaje['Contenido encriptado'] = cifrado_cesar(mensaje['Contenido'])
                return mensaje, 200
        return {'error': 'Mensaje no encontrado'}, 404

    def delete(self, id):
        global mensajes
        mensajes = [mensaje for mensaje in mensajes if mensaje['ID'] != id]
        return {'message': 'Mensaje eliminado'}, 200

api.add_resource(Mensaje, '/mensajes', '/mensajes/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
