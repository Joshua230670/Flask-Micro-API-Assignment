import requests

# URL that leads to the data page
URL = "http://127.0.0.1:5000/data"

try:
    response = requests.get(URL).json() # Attempt to get the data as json
    print(response)
except Exception as e:
    print(f"Could not fetch the data: {e}")