import requests

url = "http://127.0.0.1:8000/api/menu/componnents/1/"

payload = ""
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MjUzNjQ3LCJpYXQiOjE2OTgyNTMwNDcsImp0aSI6ImU1ZGQzYzc0NzhkYjQ0ODg5ZTZiMDZmOTc5MzlkNjRmIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJNb2hhbWVkIEF6bWkiLCJpc19zdXBlcl91c2VyIjp0cnVlLCJlbWFpbCI6InB5ZGV2YXptaUBnbWFpbC5jb20ifQ.NadkxBGWSGtQfs8D07A1lv2zHnL3N_x9znIRMsB4jH4'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
