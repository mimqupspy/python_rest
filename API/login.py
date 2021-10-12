import requests

api_url = "https://reqres.in/api/login"
response = requests.get(api_url)
print(response.status_code)
print(response.json())

# sucessfull login

valid_login = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

response = requests.post(api_url, valid_login)
login_message = response.json()
print(login_message)
print(response.status_code)
print("Response Code " + str(response.status_code))

# unsucessfull login

invalid_login = {
    "email": "eve.holt@reqres.in"
}

response = requests.post(api_url, invalid_login)
login_message = response.json()
print(login_message)
print("Response Code " + str(response.status_code))