import requests

url = "http://127.0.0.1:8000/api/menu/items/1/"

payload = ""
headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MjU0MzcwLCJpYXQiOjE2OTgyNTM3NzAsImp0aSI6ImRkYmI5YTQ3MjkyMjQzNGY4MTBlNzZhOWI0ZmFmYWU0IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJNb2hhbWVkIEF6bWkiLCJpc19zdXBlcl91c2VyIjp0cnVlLCJlbWFpbCI6InB5ZGV2YXptaUBnbWFpbC5jb20ifQ.Gmn0amqWAtEUaFxiakTwFpOiAd-Vzs6LHvLXl_CAV5Y'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
