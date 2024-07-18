import json
import jsonpath
import requests


URL = "https://reqres.in/api/users?page=2"


#sending the get request
response = requests.get(URL)

json_response = json.loads(response.text)

# print(json_response)

#Fetching Value using json Path

pages = jsonpath.jsonpath(json_response,"total_pages")

print(pages[0])

assert pages[0] == 2

for name in range(0,6):
    first_name = jsonpath.jsonpath(json_response,'data['+str(name)+'].first_name')

    print(first_name)



#printing the response content
# print(response.content)

# #printing the response header
# print(response.headers)
#
# #Fetch Specific date from the header
# print(response.headers.get('Date'))
# print(response.headers.get('Server'))
#
# #Fetch the cookies
# print(response.cookies)
#
# #Fetch the encoding
# print(response.encoding)
#
# #Fetch Elapse Time
# print(response.elapsed)

#Now Working with Json Path


assert response.status_code == 200