import requests
import json

url = "http://127.0.0.1:8000/api/auth/jwt/verify"

payload = json.dumps({
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MDA4NDE5LCJpYXQiOjE2OTgwMDgxMTksImp0aSI6ImZkOTUyNjZjNTA5OTRhMTU4NDRjMDUwZmUyMDhlM2VmIiwidXNlcl9pZCI6MX0.jPGkL4edMrOIy2bKEYbPYd0mTXwWHMHm9mieEDekBzM"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
