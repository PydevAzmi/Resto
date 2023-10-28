import requests
import json

url = "http://127.0.0.1:8000/api/menu/items/"

payload = json.dumps({
  "name": "Duetto",
  "description": "2 Chicken Pieces + 2 Rizo + 2 Kantook + 1L Drink",
  "category": "Deals",
  "price": 356,
  "image": None,
  "is_sale": True,
  "sale": 0.16,
  "ingredients": [
    "Chicken Piece",
    "Rizo",
    "Kantook",
    "Beverage 1L"
  ],
  "quantity_list": "2, 2, 2, 1" # must be in order so the result will be like that: ("Chicken Piece", 2), ("Rizo", 2), ("Kantook", 2), ("Beverage 1L", 1)
})
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MjM0NDI1LCJpYXQiOjE2OTgyMzQxMjUsImp0aSI6IjcyYjE5NDJkMDlkZjQ1N2FiOTkzNmU5OWE2NTY3YWY3IiwidXNlcl9pZCI6MX0.KFEL6AbPCWMlcrXcyRhwS151Q8PDg-sQs4EzknJP_mk',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
