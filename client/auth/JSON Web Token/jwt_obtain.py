import requests
import json

url = "http://127.0.0.1:8000/api/auth/jwt/create"

payload = json.dumps({
  "email": "pydevazmi@gmail.com",
  "password": "Python@011"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
