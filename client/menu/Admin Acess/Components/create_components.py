import requests
import json

url = "http://127.0.0.1:8000/api/menu/componnents/"

payload = json.dumps({
  "ingredient": 1,
  "name": "Chicken Piece",
  "type": "Spicy",
  "price": 0,
  "image": None
})
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MjMzMzU5LCJpYXQiOjE2OTgyMzMwNTksImp0aSI6IjFlYjQxYWUyYzYyZDRmM2ViYTk5YmE1ZTI2OTUxYzk2IiwidXNlcl9pZCI6MX0.fhj9Ld3_KmeHQZhnFXu9YSeWP3lwAy4BjhWlkEOxnVQ',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
