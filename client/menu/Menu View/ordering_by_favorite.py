import requests

url = "http://127.0.0.1:8000/api/menu/items/?ordering=-is_fav" # Descending

payload = {}
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MjYxMTM2LCJpYXQiOjE2OTgyNjA1MzYsImp0aSI6ImQ2NWI4NzAyMzZiZjQzOWE5NjQyZWMxMDE4YTJkYzEyIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJNb2hhbWVkIEF6bWkiLCJpc19zdXBlcl91c2VyIjp0cnVlLCJlbWFpbCI6InB5ZGV2YXptaUBnbWFpbC5jb20ifQ.XQ2XgcH0zIADEDDfgRk78UQKmnd_o0BVHQdnHmCtMFI'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
