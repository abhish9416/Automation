import requests
import json
import jsonpath
from Utilities import Random_data

# def getbooking():
#     url = "https://restful-booker.herokuapp.com/booking"
#
#     response = requests.get(url)
#     print(response.status_code)
#     print(response.text)
#
# getbooking()

def createbooking():
    global id
    url = "https://restful-booker.herokuapp.com/booking"
    file = open('create.json','r')
    create_json = file.read()
    json_input = json.loads(create_json)
    json_input['firstname'] = Random_data.first_name_gen()
    json_input['lastname'] = Random_data.last_name_gen()
    response = requests.post(url,json=json_input)
    print(response.status_code)
    print(response.text)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json,'bookingid')
    print(id[0])

createbooking()

def getbookingid():
    URL = "https://restful-booker.herokuapp.com/booking/"+str(id[0])
    response = requests.get(URL)
    print(response.status_code)
    print(response.text)

getbookingid()

