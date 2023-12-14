import requests
response = requests.get("https://randomuser.me/api/")
print(response.text)

import requests

api_url = "https://randomuser.me/api/"
response = requests.get(api_url)
print(response)

import requests

api_url = "https://randomuser.me/api/"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()  # Assuming the response is in JSON format
    print(data)
else:
    print(f"Error: {response.status_code}")

import json
data = json.loads (response.text)
# Extract and print the "location" information
location_info = data['results'][0]['location']
print(json.dumps(location_info, indent=2))