import requests

url = 'http://localhost:5000/animales'

animal = {
    'ID': '123',
    'Nombre': 'Simba',
    'Especie': 'León',
    'Género': 'M',
    'Edad': 5,
    'Peso': 190,
    'Tipo': 'Mamífero'
}

response = requests.post(url, json=animal)
print(response.json())
