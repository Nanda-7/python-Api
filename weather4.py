import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


API_KEY = "YOUR_API_KEY"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": "Mumbai",
    "appid": API_KEY,
    "units": "metric"
}


retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[500, 502, 503, 504],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retry_strategy)

session = requests.Session()

session.mount("https://", adapter)
session.mount("http://", adapter)


try:

    response = session.get(
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