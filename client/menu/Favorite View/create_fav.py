import requests
import json

url = "http://127.0.0.1:8000/api/menu/favorites/"

payload = json.dumps({
  "item": 1
})
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MjU1MTM4LCJpYXQiOjE2OTgyNTQ1MzgsImp0aSI6IjdjNjIwZjc2ODIzMjRlNjRiNTE0MDExYjhhZGY0MTM3IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJNb2hhbWVkIEF6bWkiLCJpc19zdXBlcl91c2VyIjp0cnVlLCJlbWFpbCI6InB5ZGV2YXptaUBnbWFpbC5jb20ifQ.MP6NlRjU2J48INRXFQZFT8puBZvKqiw6HOIXdnIIG1U',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
