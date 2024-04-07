from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

animales = []

class Animal(Resource):
    def get(self, id=None):
        if id:
            for animal in animales:
                if animal['ID'] == id:
                    return jsonify(animal)
            return {'error': 'Animal no encontrado'}, 404
        else:
            return jsonify(animales)

    def post(self):
        nuevo_animal = request.get_json()
        animales.append(nuevo_animal)
        return nuevo_animal, 201

    def put(self, id):
        for animal in animales:
            if animal['ID'] == id:
                animal.update(request.get_json())
                return animal, 200
        return {'error': 'Animal no encontrado'}, 404

    def delete(self, id):
        global animales
        animales = [animal for animal in animales if animal['ID'] != id]
        return {'message': 'Animal eliminado'}, 200

api.add_resource(Animal, '/animales', '/animales/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
