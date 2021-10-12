import requests
import testdata.api_endpoint

delayed_url = testdata.api_endpoint.get_delayed_url
response = requests.get(delayed_url)
delayed_response_code = response.status_code
# print(response.status_code)
# print(response.json())
print(delayed_response_code)

