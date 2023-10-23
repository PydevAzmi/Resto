import requests

api_url = "http://127.0.0.1:8000/api/menu/items/"

response = requests.get(api_url)
response.json()
