import requests
import json

url = "http://127.0.0.1:8000/api/auth/jwt/refresh"

payload = json.dumps({
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5ODA5Mjc5NCwiaWF0IjoxNjk4MDA2Mzk0LCJqdGkiOiI1ZTkzNGI2NTFiM2Y0NmZkOTgwNzU2NjQ1YTRiMzI0NCIsInVzZXJfaWQiOjF9.vSud0KjwBaSOATeEKdeOww9tAArM5uky-Sy5pedCDbQ"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
