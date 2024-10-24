import requests

url = "http://127.0.0.1:8000/api/properties/"
data = {
    "address": "123 Main St",
    "city": "Charlotte",
    "state": "NC",
    "price": 300000.00,
    "description": "Beautiful family home in a quiet neighborhood."
}

response = requests.post(url, json=data)
print(response.json())
