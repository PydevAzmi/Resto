import requests
import json

url = "http://127.0.0.1:8000/api/auth/users/set_email/"

payload = json.dumps({
  "current_password": "12345",
  "new_email": "admin@gmail.com",
  "re_new_email": "admin@gmail.com"
})
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MDIzODcwLCJpYXQiOjE2OTgwMjM1NzAsImp0aSI6IjFhOWNiMTZhOGE4YzQzM2NiNWIyMmUyMTdmM2ZhYzdjIiwidXNlcl9pZCI6MX0.3FuGR4lJIi_f51DqGuteiaiePMcD7ZU6PY8TaOkzdQ8',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
