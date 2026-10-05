import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print(response.status_code)

user = response.json()

print(user)
print(user["name"])
print(user["email"])
print(user["company"]["name"])