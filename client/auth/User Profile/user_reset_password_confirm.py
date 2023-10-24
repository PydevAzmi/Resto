import requests
import json

url = "http://127.0.0.1:8000/api/auth/users/reset_password_confirm/"

payload = json.dumps({
  "uid": "ED",
  "token": "bwi9ux-f73e0d58690fb128c40cb25e1b6cf30f",
  "new_password": "This Is My New Unhackable Password"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
