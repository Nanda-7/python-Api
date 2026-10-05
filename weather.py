import requests

API_KEY = "YOUR_API_KEY"

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