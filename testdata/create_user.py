import requests
import testdata.api_endpoint

users_data = {
    "name": "demouser",
    "job": "SRE"
}


# create user
create_user_url = testdata.api_endpoint.post_create_user_url
create_user_url_response = requests.post(create_user_url,users_data)
create_user_url_code = create_user_url_response.status_code
create_user_url_data = create_user_url_response.json()
# print(create_user_url_data)

