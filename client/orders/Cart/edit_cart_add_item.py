import requests
import json

url = "http://127.0.0.1:8000/api/orders/cart/4/"

payload = json.dumps({
  "item": "Duetto",
  "quantity": 4
})
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4NDA2OTk1LCJpYXQiOjE2OTg0MDYzOTUsImp0aSI6ImFkMjhhYzA5ZDMwYTRjNDM4ZGRiNTFhNTFmMGJlZTVkIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJNb2hhbWVkIEF6bWkiLCJpc19zdXBlcl91c2VyIjp0cnVlLCJlbWFpbCI6InB5ZGV2YXptaUBnbWFpbC5jb20ifQ.ZGp1nqzTnpE1D-hUY6_d6do7MV6tWF0JSppSsDN-H3c',
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
