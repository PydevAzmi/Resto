import requests
import json

url = "http://127.0.0.1:8000/api/menu/ingredients/2/"

payload = json.dumps({
  "is_optional": False
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
