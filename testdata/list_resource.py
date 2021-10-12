import requests
import testdata.api_endpoint

# list resource
list_resource_url = testdata.api_endpoint.list_resource
list_resource_response = requests.get(list_resource_url)
list_resource_response_code = list_resource_response.status_code
list_resource_data = list_resource_response.json()
# print(response_code)
# print(list_resource_data["total_pages"])

# single resource
single_resource_url = testdata.api_endpoint.single_resource
single_resource_response = requests.get(single_resource_url)
single_resource_response_code = single_resource_response.status_code
single_resource_data = single_resource_response.json()
# print("color" in single_resource_data["data"])


# single resource not found
single_resource_not_found_url = testdata.api_endpoint.single_resource_not_found
single_resource_not_found_response = requests.get(single_resource_not_found_url)
single_resource_not_found_code = single_resource_not_found_response.status_code
single_resource_not_found_data = single_resource_not_found_response.json()

