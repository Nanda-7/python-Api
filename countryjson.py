import requests

url = "https://api.restcountries.com/countries/v5/names.common/Canada"

headers = {
    "Authorization": "Bearer rc_live_demo"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())