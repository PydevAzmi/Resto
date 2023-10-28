import requests
import json

url = "http://127.0.0.1:8000/api/menu/categories/"

payload = json.dumps({
  "name": "For One",
  "image": None
})
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MjQ1MjQyLCJpYXQiOjE2OTgyNDQ5NDIsImp0aSI6ImY4YTA1NjEwNjA5OTQ0NzliM2EwYWZhZDcxNTEwMmE0IiwidXNlcl9pZCI6MX0.Jx6t7vAsyw6I34jwIyFmUYKRUSwwmAaZyFZ_cN2avvc',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
2
print(response.text)
