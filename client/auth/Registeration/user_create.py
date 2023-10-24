import requests
import json

url = "http://127.0.0.1:8000/api/auth/users/"

payload = json.dumps({
  "email": "pydevazmii@gmail.com",
  "username": "Mohamed Azmi",
  "phone_number": "+201126732635",
  "password": "Python@011",
  "re_password": "Python@011"
})
headers = {
  'content-type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
