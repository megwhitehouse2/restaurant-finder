import requests
import json

url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers = headers)
data = response.json()

# Checking the structure of the API like what are the top level keys, number of restaurants, etec
# and inspect what is returned from an individual restaurant
print("Top level keys:", data.keys())
print("Number of restaurants:", len(data["restaurants"]))
print(json.dumps(data["restaurants"][0], indent=2))
