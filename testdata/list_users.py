import requests
import testdata.api_endpoint

# list user url
list_user_url = testdata.api_endpoint.list_user
response = requests.get(list_user_url)
response_code = response.status_code
data = response.json()
# print(response_code)
# print(data["data"])

# single user
single_user = testdata.api_endpoint.single_user
single_user_req = requests.get(single_user)
single_user_response_code = single_user_req.status_code
single_user_data = single_user_req.json()
# print(single_user_response_code)
# print(single_user_data["data"]["first_name"])


# single user not found
single_user_not_found = testdata.api_endpoint.single_user_not_found
single_user_not_found_req = requests.get(single_user_not_found)
single_user_not_found_response_code = single_user_not_found_req.status_code
single_user_not_found_data = single_user_not_found_req.json()
# print(single_user_not_found_data)










