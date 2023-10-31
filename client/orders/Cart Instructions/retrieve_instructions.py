import requests

url = "http://127.0.0.1:8000/api/orders/cart/3/instructions/1"

payload = {}
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MzE5Mzk4LCJpYXQiOjE2OTgzMTg3OTgsImp0aSI6ImFjMGFlNjJlOGZmNzQyZTFhYmRjMWQxMmE2ZmRlODIxIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJNb2hhbWVkIEF6bWkiLCJpc19zdXBlcl91c2VyIjp0cnVlLCJlbWFpbCI6InB5ZGV2YXptaUBnbWFpbC5jb20ifQ.SAYFz6jFiX8wPQbos0XgHYKl65MWsIHZ9muTucoAzrU'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
