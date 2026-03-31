# Coding Project: Restaurant Finder

This is a simple web app made using Flask, which searches for UK restaurants with their postcode and returns their name, cuisines, rating and address (first 10 results), which is done using the `JustEat API`. 

## Requirements
- *Python 3.8+*
- *Flask*
- *requests*

Install dependencies with:
```bash
pip3 install flask requests
```

## How to run
```bash
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000
```

Enter any UK postcode (e.g. `EC4M 7RF`) and hit Search.

## How does it work?

1. The user will enter a postcode in the search form
2. Flask receives the form submission and then passes the postcode to the API function
3. The postcode is sanitised (spaces stripped, uppercased) before being sent to the `JustEat API`
4. The `API` returns a `JSON` response containing restaurant data
5. The app extracts name, cuisines, rating and address for the first 10 restaurants
6. Results are passed to the `HTML template` and displayed as cards in the browser
   
-----------------------------------------------------------------------------------------------------------------------------------------------
## Implementation
In my code, I need to:
1.  Check `API` response structure to understand the structure of what is being returned and why
2.  Identify which of these fields map to the requirements (name, rating as a number, cuisine, address) with a limit of 10 restaurants returned
3.  Map data flow from postcode input to display

### Assumptions
- Endpoint returns restaurant objects so no type filtering beyond limiting to 10 was needed
- Postcodes are sanitised (e.g., spaces stripped and uppercased) before being passed to the `API`

- Potential edge cases to handle:
---------------------------------
- For an invalid postcode, an error message would be displayed. 
- Missing rating on a restaurant would display no rating if there was no edge case
- If there are issues in the postcode, it would be stripped automatically

Improvements?
1. Filter promotional cuisine tags like 'deals' or whether someone in a regular customer or not
2. Be able to sort by rating. Also have some kind of integration with google reviews.
3. Double check data extraction through unit testing
4. Add something to display the status of the API, e.g. add a loading state whilst it fetches
5. Be able to look at the menu of the place/website from within the app. 




Supplementary info, e.g. from exploring the API or notes made during the process
## 1. API characteristics

After running the `explore_api.py` file.
-data['restaurants'] --> 2264 total
-r['name]: string
-r["address"]["firstLine"], r["address"]["city"],
 r["address"]["postalCode"] are all nested one level down.
r['rating']['starRating'] nested
r['cuisines'] is the list of objects and each has a name key

In the cuisines field we get:
*{"name": "Collect stamps", "uniqueName": "stampcard-restaurants"}*, this is likely a promotional tag?

