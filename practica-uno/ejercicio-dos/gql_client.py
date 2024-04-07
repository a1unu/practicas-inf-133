import requests
import json

url = 'http://localhost:5000/graphql'

query = '''
{
  plantas {
    id
    nombre_comun
    especie
    edad
    altura
    frutos
  }
}
'''

response = requests.post(url, json={'query': query})
print(json.dumps(response.json(), indent=2))
