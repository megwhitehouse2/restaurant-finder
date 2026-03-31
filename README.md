##API characteristics

After running the `explore_api.py` file.
-data['restaurants'] --> 2264 total
-r['name]: string
-r["address"]["firstLine"], r["address"]["city"],
 r["address"]["postalCode"] are all nested one level down.
r['rating']['starRating'] nested
r['cuisines'] is the list of objects and each has a name key

In the cuisines field we get:
*{"name": "Collect stamps", "uniqueName": "stampcard-restaurants"}*, this is likely a promotional tag?