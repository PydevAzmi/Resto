import requests
import json

url = "http://127.0.0.1:8000/api/auth/users/resend_activation/"

payload = json.dumps({
  "email": "pydevazmi@gmail.com"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
