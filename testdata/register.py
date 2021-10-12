import requests
import testdata.api_endpoint

valid_register = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

invalid_register = {
    "email": "eve.holt@reqres.in",
}

# Register Successful
register_url = testdata.api_endpoint.register_url
register_url_response = requests.post(register_url,valid_register)
register_url_code = register_url_response.status_code
register_url_data = register_url_response.json()
print(register_url_data)
print(register_url_response)


# Register UnSuccessful
un_register_url = testdata.api_endpoint.register_url
un_register_url_response = requests.post(un_register_url,invalid_register)
un_register_url_code = un_register_url_response.status_code
un_register_url_data = un_register_url_response.json()
print(un_register_url_code)
print(un_register_url_data)


