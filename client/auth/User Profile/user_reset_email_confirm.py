import requests
import json

url = "http://127.0.0.1:8000/api/auth/users/reset_email_confirm/"

payload = json.dumps({
  "uid": "MQ",
  "token": "bwi9ux-f73e0d58690fb128c40cb25e1b6cf30f",
  "new_email": "py@gmail.com"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
