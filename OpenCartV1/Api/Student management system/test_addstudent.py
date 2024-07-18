import json
import requests
import jsonpath

def addStudent():
    URL = "https://thetestingworldapi.com/api/Students"
    file = open("add_student.json",'r')
    json_input = json.loads(file.read())
    response = requests.post(URL,json_input)
    print(response.text)
    print(response.status_code)


addStudent()