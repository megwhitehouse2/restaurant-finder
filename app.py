import requests
from flask import Flask, render_template, request

app = Flask(__name__)
API = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{}"

# Function to call the Just Eat API and extract restaurant data
def get_restaurants(postcode):
    clean = postcode.replace(" ", "").upper()
    url = API.format(clean)
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    data = response.json()

    restaurants = data.get("restaurants", [])[:10]

    results = []
    for r in restaurants:
        address = r.get("address", {})
        rating = r.get("rating", {})
        cuisines = r.get("cuisines", [])

        results.append({
            "name": r.get("name", "Unknown"),
            "cuisines": [c["name"] for c in cuisines if "name" in c],
            "rating": rating.get("starRating"),
            "address": ", ".join(filter(None, [
                address.get("firstLine"),
                address.get("city"),
                address.get("postalCode")
            ]))
        })

    return results, data.get("metaData", {}).get("area", clean)

#Using flask to handle the page loading and form submission
@app.route("/", methods=["GET", "POST"])
def index():
    restaurants = []
    area = None
    error = None
    postcode = ""

    if request.method == "POST":
        postcode = request.form.get("postcode", "").strip()
        if postcode:
            try:
                restaurants, area = get_restaurants(postcode)
                if not restaurants:
                    error = "No restaurants found for that postcode."
            except requests.exceptions.HTTPError:
                error = "Could not find results for that postcode. Please check and try again."
            except Exception:
                error = "Something went wrong. Please try again."

    return render_template("index.html",
                           restaurants=restaurants,
                           area=area,
                           error=error,
                           postcode=postcode)

if __name__ == "__main__":
    app.run(debug=True)