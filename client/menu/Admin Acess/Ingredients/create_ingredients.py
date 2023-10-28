import requests
import json

url = "http://127.0.0.1:8000/api/menu/ingredients/"

payload = json.dumps({
  "name": "Fries Or Coleslaw",
  "is_optional": False
})
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MjMyODM2LCJpYXQiOjE2OTgyMzI1MzYsImp0aSI6ImQ5M2ExZjQ1OGI2ODQ1ZmNhMjI3NmU4MmI5NzQyZjk1IiwidXNlcl9pZCI6MX0.11FdRZvPY1C6ez2QgkBIRaY8dzQumRhNGw6lt_6FspU',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
