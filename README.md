## Project overview
1. Check API response structure to understand the structure of what is being returned and why
2. Identify which of these fields map to the requirements (name, rating as a number, cuisine, address) with a limit of 10 restaurants returned
3. Map data flow from postcode input to display

### Assumptions
- Endpoint returns restaurant objects so no type filtering beyond limiting to 10 was needed
- Postcodes are sanitised (e.g., spaces stripped and uppercased) before being passed to the API

- Potential edge cases:
- For an invalid postcode, an error message would be displayed. 
- Missing rating on a restaurant would display no rating if there was no edge case
- If there are issues in the postcode, it would be stripped automatically

Improvements?
1. Filter promotional cuisine tags like 'deals' or whether someone in a regular customer or not
2. Be able to sort by rating
3. Double check data extraction through unit testing
4. Add something to display the status of the API, e.g. add a loading state whilst it fetches

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

