import requests
import json
import jsonpath

URL = "https://reqres.in/api/users"

file = open('Createuser.json','r')
json_input = file.read()

create_user = json.loads(json_input)

response = requests.post(URL,create_user)

print(response.content)
print(response.status_code)

#Fetch Header of the response
print(response.headers)

#Parse response to json format
json_response = json.loads(response.text)

#Pick Id using json path
id = jsonpath.jsonpath(json_response,'id')
print(id)