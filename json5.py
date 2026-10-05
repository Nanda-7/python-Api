import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    users = response.json()

    for user in users:
        print(user["name"])

except requests.exceptions.RequestException as e:
    print("Request failed:", e)