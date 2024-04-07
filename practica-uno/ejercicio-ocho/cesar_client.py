import requests

url = 'http://localhost:5000/mensajes'

# Crear un mensaje
nuevo_mensaje = {
    'ID': '123',
    'Contenido': 'hola mundo'
}

response = requests.post(url, json=nuevo_mensaje)
print('POST /mensajes', response.json())

# Listar todos los mensajes
response = requests.get(url)
print('GET /mensajes', response.json())

# Buscar mensajes por ID
response = requests.get(url + '/123')
print('GET /mensajes/123', response.json())

# Actualizar el contenido de un mensaje
actualizacion_mensaje = {
    'Contenido': 'adios mundo'
}
response = requests.put(url + '/123', json=actualizacion_mensaje)
print('PUT /mensajes/123', response.json())

# Eliminar un mensaje
response = requests.delete(url + '/123')
print('DELETE /mensajes/123', response.json())
