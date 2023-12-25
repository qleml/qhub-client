import requests

# URL of the local server
url = "http://localhost:3000/api"

# Making a GET request
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    print("Success:", response.text)
else:
    print("Error:", response.status_code)
