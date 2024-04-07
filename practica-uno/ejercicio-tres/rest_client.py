import requests

url = 'http://localhost:5000/pacientes'

# Crear un paciente
nuevo_paciente = {
    'CI': '12345678',
    'Nombre': 'Juan',
    'Apellido': 'Perez',
    'Edad': 30,
    'Género': 'M',
    'Diagnóstico': 'Diabetes',
    'Doctor': 'Pedro Pérez'
}
response = requests.post(url, json=nuevo_paciente)
print('POST /pacientes', response.json())

# Listar todos los pacientes
response = requests.get(url)
print('GET /pacientes', response.json())

# Buscar pacientes por CI
response = requests.get(url + '/12345678')
print('GET /pacientes/12345678', response.json())

# Actualizar la información de un paciente
actualizacion_paciente = {
    'Nombre': 'Juanito'
}
response = requests.put(url + '/12345678', json=actualizacion_paciente)
print('PUT /pacientes/12345678', response.json())

# Eliminar un paciente
response = requests.delete(url + '/12345678')
print('DELETE /pacientes/12345678', response.json())
