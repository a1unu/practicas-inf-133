
import requests

url = 'http://localhost:5000/partidas'

partida = {
    'elemento': 'piedra'
}

response = requests.post(url, json=partida)
print(response.json())
