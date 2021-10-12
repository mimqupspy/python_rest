import requests
import testdata.api_endpoint

users_data = {
    "name": "adminuser",
    "job": "Admin"
}


# put user
put_user_url = testdata.api_endpoint.put_user
put_user_url_response = requests.put(put_user_url,users_data)
put_user_url_code = put_user_url_response.status_code
put_user_url_data = put_user_url_response.json()
print(put_user_url_data)
print(put_user_url_response)

