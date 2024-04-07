from suds.client import Client
from suds.sudsobject import asdict

url = 'http://127.0.0.1:8000/?wsdl'
client = Client(url)

def print_result(operation, a, b, result):
    print(f"{operation}: {a} {operation_symbols[operation]} {b} = {result}")

operation_symbols = {
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "divide": "/",
}

operations = [
    ("add", 5, 3),
    ("subtract", 10, 4),
    ("multiply", 6, 7),
    ("divide", 15, 3),
]

for operation, a, b in operations:
    try:
        result = asdict(getattr(client.service, operation)(a, b))["value"]
        print_result(operation, a, b, result)
    except Exception as e:
        print(f"Error en {operation}: {e}")