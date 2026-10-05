import requests

API_KEY = "YOUR_API_KEY"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": "Hyderabad",
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)

print("Status:", response.status_code)

data = response.json()

print("City:", data["name"])
print("Temperature:", data["main"]["temp"], "°C")
print("Humidity:", data["main"]["humidity"], "%")
print("Weather:", data["weather"][0]["description"])