import requests

def get_place(query, location, API_KEY):
    # API endpoint
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    # Query parameters
    params = {
        "query": query,
        "location": location,
        "key": API_KEY
    }

    # Make the request
    response = requests.get(url, params=params)

    # Check the status code
    if response.status_code == 200:
        # Get the response data
        data = response.json()

        # Extract the first result
        result = data.get("results", [None])

        return result
    else:
        # Raise an error if the request failed
        raise Exception("Request failed with status code: " + str(response.status_code))

# Example usage
"""
query = "Empire State Building, New York"
location = "40.7128,-74.0060"
API_KEY = "YOUR_API_KEY"

result = get_place(query, location, API_KEY)

if result:
    print(result["name"], result["formatted_address"])
else:
    print("No results found.")
"""
