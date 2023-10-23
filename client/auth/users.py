import requests

# if Admin list all Users
url = "http://127.0.0.1:8000/api/auth/users/"

payload = {}
headers = {
  'Authorization': 
  'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MDE0MTMwLCJpYXQiOjE2OTgwMTM4MzAsImp0aSI6IjY5OGFiZDY2NGQxYjRiOTY4ZDUzNmEyMjYzYTE2NTc5IiwidXNlcl9pZCI6MX0.aCtYqlSvHt5F7wjxDM0W1t3tSQadxbeyom3TAfJKldE'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

