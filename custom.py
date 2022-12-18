import requests
endpoint = "http://127.0.0.1:8000/api/v1/todo"
response=requests.get(endpoint)
res = (response.json())
print(res)
