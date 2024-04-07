import requests

url = 'http://localhost:5000/animales'

# Crear un animal
nuevo_animal = {
    'ID': '123',
    'Nombre': 'Simba',
    'Especie': 'León',
    'Género': 'M',
    'Edad': 5,
    'Peso': 190
}
response = requests.post(url, json=nuevo_animal)
print('POST /animales', response.json())

# Listar todos los animales
response = requests.get(url)
print('GET /animales', response.json())

# Buscar animales por ID
response = requests.get(url + '/123')
print('GET /animales/123', response.json())

# Actualizar la información de un animal
actualizacion_animal = {
    'Nombre': 'Simba Jr.'
}
response = requests.put(url + '/123', json=actualizacion_animal)
print('PUT /animales/123', response.json())

# Eliminar un animal
response = requests.delete(url + '/123')
print('DELETE /animales/123', response.json())
