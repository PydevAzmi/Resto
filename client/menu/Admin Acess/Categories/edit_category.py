import requests
import json

url = "http://127.0.0.1:8000/api/menu/categories/2/"

payload = json.dumps({
  "image": None
})
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MjQ1NTUzLCJpYXQiOjE2OTgyNDUyNTMsImp0aSI6IjgxMTEzYjkzZDIxZTQ4ZjliNzEzMDU2NDM1OTNjMTY1IiwidXNlcl9pZCI6MX0.LrBleNLzsfnIXNB3psCDGzmIG94glRNl5ioBK_GV_Vo',
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
