import requests
import testdata.api_endpoint

users_data = {
    "name": "demouser",
    # "job": "SRE"
}


# delete user
delete_user_url = testdata.api_endpoint.delete_user_url
delete_user_url_response = requests.delete(delete_user_url,users_data)
delete_user_url_code = delete_user_url_response.status_code
delete_user_url_data = delete_user_url_response.json()
print(delete_user_url_data)

