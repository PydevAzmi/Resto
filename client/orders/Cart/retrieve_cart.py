import requests

url = "http://127.0.0.1:8000/api/orders/cart/3/"

payload = {}
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MzE4NTM0LCJpYXQiOjE2OTgzMTc5MzQsImp0aSI6ImI5ZGY0ZWFmNjhmYzRmYjBhZGVmYzU2MjY1MjE4MTU3IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJNb2hhbWVkIEF6bWkiLCJpc19zdXBlcl91c2VyIjp0cnVlLCJlbWFpbCI6InB5ZGV2YXptaUBnbWFpbC5jb20ifQ.t90qO1QMgJlyxTn7hZAoS1Lt7oJgR1aijrHQSGExVbU'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
