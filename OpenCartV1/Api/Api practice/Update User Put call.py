import json
import jsonpath
import requests

#Put Api URL for Updating the user
URL = "https://reqres.in/api/users/2"

#Reading the Data from the input file
file = open("Createuser.json",'r')

#Parsing the file into json input
json_input = json.loads(file.read())

#Hitting the put Method
response = requests.put(URL,json_input)


#printing the Api Response
print(response.text)
print(response.content)
print(response.status_code)

#validating the api response

#parsing the response into json format

json_response = json.loads(response.text)

#finding the Updated with the json path

json_updated = jsonpath.jsonpath(json_response,'updatedAt')
print(json_updated)