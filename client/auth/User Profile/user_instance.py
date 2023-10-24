import requests

url = "http://127.0.0.1:8000/api/auth/users/me/"

payload = ""
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MDIzODcwLCJpYXQiOjE2OTgwMjM1NzAsImp0aSI6IjFhOWNiMTZhOGE4YzQzM2NiNWIyMmUyMTdmM2ZhYzdjIiwidXNlcl9pZCI6MX0.3FuGR4lJIi_f51DqGuteiaiePMcD7ZU6PY8TaOkzdQ8'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
