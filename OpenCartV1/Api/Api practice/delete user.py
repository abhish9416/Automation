import requests

URL = "https://reqres.in/api/users/2"

response = requests.delete(URL)

#Fetch Status code

print(response.status_code)

assert response.status_code == 204