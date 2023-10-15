import requests

api_url = "http://127.0.0.1:8000/api/orders/cart"

response = requests.get(api_url)
print(response.json())