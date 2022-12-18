import requests
from getpass import getpass

auth_url = 'http://127.0.0.1:8000/api-token-auth/'

username = input('Your username: ')
password = getpass("Enter your password: ")

auth_response = requests.post(auth_url, json={"username": username, "password":password})
print(auth_response.json())
if auth_response.status_code == 200:
    token = auth_response.json()['token']
    with open("token.txt", 'w') as file:
        file.writelines(f'Token {token}')
    headers = {
        'Authorization': f'Token {token}'
    }

    endpoint = 'http://127.0.0.1:8000/api/v1/todo/list&create'
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())


