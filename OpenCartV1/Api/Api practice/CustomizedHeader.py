import json
import jsonpath
import requests


URL = "https://httpbin.org/get"

headerdata = {"T1":"First header","T2":"Second Header"}

response = requests.get(URL,headers=headerdata)

print(response.text)