import requests
URL = "https://httpbin.org/get"

headerdata = {"T1":"First header","T2":"Second Header"}

response = requests.get(URL,params=headerdata)

print(response.text)