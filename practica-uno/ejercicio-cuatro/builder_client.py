import requests

url = 'http://localhost:5000/pacientes'

paciente = {
    'ci': '12345678',
    'nombre': 'Juan',
    'apellido': 'Perez',
    'edad': 30,
    'genero': 'M',
    'diagnostico': 'Diabetes',
    'doctor': 'Pedro Pérez'
}

response = requests.post(url, json=paciente)
print(response.json())
