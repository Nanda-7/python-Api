import requests

url = "https://api.restcountries.com/countries/v5/names.common/India"

headers = {
    "Authorization": "Bearer rc_live_demo"
}

response = requests.get(url, headers=headers, timeout=5)
response.raise_for_status()

data = response.json()
country = data["data"]["objects"][0]

print("Country:", country["names"]["common"])
print("Capital:", country["capitals"][0])
print("Population:", country["population"])
print("Region:", country["region"])