import requests
from place import get_place

def get_places(place_type, query, location, radius, API_KEY):
    # API endpoint
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    # Query parameters
    params = {
        "query": query,
        "location": location,
        "radius": radius,
        "key": API_KEY,
        "type": place_type
    }

    # Make the request
    response = requests.get(url, params=params)

    # Check the status code
    if response.status_code == 200:
        # Get the response data
        data = response.json()

        # Extract the results
        results = data.get("results", [])

        return results
    else:
        # Raise an error if the request failed
        raise Exception("Request failed with status code: " + str(response.status_code))


def get_single_location(place_type, query, location, radius, API_KEY):
    # API endpoint
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    # Query parameters
    params = {
        "query": query,
        "location": location,
        "radius": radius,
        "key": API_KEY,
        "type": place_type
    }

    # Make the request
    response = requests.get(url, params=params)

    # Check the status code
    if response.status_code == 200:
        # Get the response data
        data = response.json()

        # Extract the results
        results = data.get("results", [])

        return results
    else:
        # Raise an error if the request failed
        raise Exception("Request failed with status code: " + str(response.status_code))

# Example usage
place_type = 'accounting'
query = "accountants in Dallas"
location = "32.963200,-96.820880"
radius = 5000
MY_KEY = "AIzaSyAe6aGkSq0sepqYeMhPtUhEEfYhwDXeIsM"

results = get_places(place_type, query, location, radius, MY_KEY)

lat_list = []
lng_list = [] 
coords_list = []
name_list = {}
addr_list = []

for result in results:
    # print(result["name"], result["formatted_address"])
    name_list = name_list.append(f'{result["name"]}: {result["geometry"]["location"]["lat"]}, {result["geometry"]["location"]["lng"]}')

for i in name_list:
    print(i)

# for result in results:
#     cord_result = f'{result["geometry"]["location"]["lat"]}, {result["geometry"]["location"]["lng"]}'
#     # coords_list += result["geometry"]["location"]["lat"] result["geometry"]["location"]["lng"]
#     coords_list += cord_result
#     # lng += 
#     name_list += f'{result["name"]}'
#     addr_list+= result["formatted_address"]
#     # print(f"{coords_list} {name_list} {addr_list}")

# for i in range(0, len(name_list)):
#     print(f"{coords_list[i]} {name_list[i]} {addr_list[i]}")
    # place_result = get_place(name_list[i], coords_list[i], MY_KEY)
    # if place_result:
    #     print(result["name"], result["formatted_address"])
    # else:
    #     print("No results found.")
    

    # print(result.get("website", "N/A"))
    # try:
        
    #     print(result["website"])
    #     # print(result["formatted_phone_number"])
    # except KeyError as e:
    #     print(f'KeyError: {e} not found')
    # try:
        
    #     # print(result["website"])
    #     print(result["formatted_phone_number"])
    # except KeyError as e:
    #     print(f'KeyError: {e} not found')
