import requests

API_KEY = "ecbda5b26a44cbc10ebd5a1c3c93e801"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": "Hyderabad",
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())

data = response.json()
print(type(data))
temp = data["main"]["temp"]
print("temp:",temp)
print(data["main"]["humidity"])