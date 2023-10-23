import requests

url = "http://127.0.0.1:8000/api/orders/cart"

headers = {
  'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MDA3NjE2LCJpYXQiOjE2OTgwMDczMTYsImp0aSI6ImNmMjY4M2Q0ZmNmMDQ1OWJiYWY3MmM5NzRjOTg3YmQ1IiwidXNlcl9pZCI6MX0.rROyjWzPgoKEhiftyHkV-QfVbdbHxK5y1zItGnaP-VQ'
}

response = requests.request("GET", url, headers=headers)

print(response.text)