import requests
import json

url = "http://127.0.0.1:8000/api/auth/users/activation/"

payload = json.dumps({
  "uid": "MQ",
  "token": "bwhv0s-3744c6cb432255c042fc50c5201e376d"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
