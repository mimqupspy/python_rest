import requests
import testdata.api_endpoint

valid_register = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

invalid_register = {
    "email": "eve.holt@reqres.in",
}

# login Successful
login_url = testdata.api_endpoint.login_url
login_url_response = requests.post(login_url,valid_register)
login_url_code = login_url_response.status_code
login_url_data = login_url_response.json()
print(login_url_data)
print(login_url_code)


# login UnSuccessful
un_login_url = testdata.api_endpoint.login_url
un_login_url_response = requests.post(un_login_url,invalid_register)
un_login_url_code = un_login_url_response.status_code
un_login_url_data = un_login_url_response.json()
print(un_login_url_code)
print(un_login_url_data)


