import requests
from testdata.api_endpoint import *


api_url = "https://reqres.in/api/register"
response = requests.get(api_url)
print(response.status_code)
print(response.json())

# sucessfull
reg = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

response = requests.post(api_url, reg)
register = response.json()
print(register)
print(response.status_code)


# unsucessfull
reg2={
    "email": "sydney@fife"
}

response = requests.post(api_url, reg2)
register_un = response.json()
print(register_un)
print(response.status_code)




