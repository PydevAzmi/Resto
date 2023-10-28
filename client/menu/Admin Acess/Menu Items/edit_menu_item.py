import requests
import json

url = "http://127.0.0.1:8000/api/menu/items/1/"

payload = json.dumps({
  "ingredients": [
    "Chicken Piece",
    "Rizo",
    "Kantook",
    "Beverage 1L"
  ],
  "quantity_list": "2, 2, 2, 1"
})
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MjU0MzcwLCJpYXQiOjE2OTgyNTM3NzAsImp0aSI6ImRkYmI5YTQ3MjkyMjQzNGY4MTBlNzZhOWI0ZmFmYWU0IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJNb2hhbWVkIEF6bWkiLCJpc19zdXBlcl91c2VyIjp0cnVlLCJlbWFpbCI6InB5ZGV2YXptaUBnbWFpbC5jb20ifQ.Gmn0amqWAtEUaFxiakTwFpOiAd-Vzs6LHvLXl_CAV5Y',
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
