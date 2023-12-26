import requests

# URL of the local server
base_url = "http://localhost:3000/api"

def check_api_response(response):
    """Check if the API response was successful"""
    if response.status_code == 200:
        print("Success:", response.text)
    else:
        print("Error:", response.status_code)

# Making a GET request
response = requests.get(base_url)
check_api_response(response)

while(True):
    # Making a POST request
    name = input("Enter your name: ")

    response = requests.post(base_url + "/algs", json={"name": name})
    check_api_response(response)
