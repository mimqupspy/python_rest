import requests
import testdata.api_endpoint

users_data = {
    "name": "morpheus",
    "job": "zion resident"
}


# patch user
patch_user_url = testdata.api_endpoint.patch_user_url
patch_user_url_response = requests.patch(patch_user_url,users_data)
patch_user_url_code = patch_user_url_response.status_code
patch_user_url_data = patch_user_url_response.json()
# print(patch_user_url_data)
print(patch_user_url_code)

