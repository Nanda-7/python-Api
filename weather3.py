import requests

API_KEY = "YOUR_API_KEY"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": "Hyderabad",
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(
        url,
        params=params,
        timeout=5
    )

    response.raise_for_status()

    data = response.json()

    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])

except requests.exceptions.RequestException as e:
    print("API request failed:", e)