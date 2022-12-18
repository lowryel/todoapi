import requests
endpoint = "http://127.0.0.1:8000/api/v1/todo/list/"
data = {
    "task": "Fun time",
    "user": 2,
}
response = requests.get(endpoint, json=data)
res = (response.json())
print(res[:3])
