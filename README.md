# Week 3 — Python API Integration

Learning how to use Python's `requests` library to interact with REST APIs.

## Topics Covered

* HTTP GET requests
* HTTP POST requests
* Query parameters
* Request headers
* JSON request/response data
* HTTP status codes
* Error handling
* Request timeouts
* API retries
* API keys

## APIs Used

### 1. JSONPlaceholder

Used for practicing basic API requests.

* GET users
* GET posts using query parameters
* POST data
* Process JSON responses

### 2. REST Countries

Used for practicing real-world JSON data.

Extracted:

* Country name
* Capital
* Population
* Region
* Other country information

### 3. OpenWeather

Used for practicing a real-world API requiring an API key.

Extracted:

* City
* Temperature
* Humidity
* Weather description

Practiced:

* API authentication using an API key
* Query parameters
* JSON data extraction
* Error handling
* Timeouts
* Retries

## Python Libraries

```text
requests
```

Install with:

```bash
pip install requests
```

## Project Structure

```text
week3-api/
│
├── jsonplaceholder.py
├── rest_countries.py
├── weather.py
├── requirements.txt
└── README.md
```

## Key Learning

The basic API integration flow:

```text
Python
   ↓
requests.get() / requests.post()
   ↓
REST API
   ↓
HTTP response
   ↓
JSON
   ↓
Python dictionary/list
   ↓
Extract and process data
```

## Example

```python
response = requests.get(
    url,
    params=params,
    timeout=5
)

response.raise_for_status()


- Session → Reuses connections and holds request configuration.
- HTTPAdapter → Applies retry configuration to HTTP requests.
- Retry → Defines when and how many times to retry.
- Backoff → Defines waiting time between retries.
- Timeout → Prevents waiting indefinitely for a response.


1. Why use requests.Session()?
A session allows you to reuse connections across multiple API calls.
session = requests.Session()response = session.get(url)

Benefits:
- Reuses TCP connections (faster for repeated calls).
- Maintains cookies and common headers.
- Supports configuring retries through adapters.

2. Why use HTTPAdapter?
An adapter controls how the session handles HTTP connections.
adapter = HTTPAdapter(max_retries=retry_strategy)session.mount("https://", adapter)
This tells Python:

Whenever an HTTPS request is made, use this adapter with the configured retry rules.

weather4.py is production level api design with session, adapter and retry mechanism.
