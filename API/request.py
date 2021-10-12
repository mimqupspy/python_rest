import requests

api_url = "https://reqres.in/api/unknown/23"
response = requests.get(api_url)
print(response.status_code)
print(response.json())

# assert (response.status_code == 400)


# create user
users = {
    "name": "morpheus",
    "job": "leader"
}
response = requests.post(api_url, users)
user = response.json()
print(user)
print(user["name"])
print(user["job"])
assert user["name"] == "morpheus"


# PUT (Update)
user2 = {
    "name": "joy",
    "job": "SRE"
}
response = requests.put(api_url, user2)
new_user = response.json()
print(new_user)
assert new_user["name"] == "joy"
print(response.status_code)


# PATCH
user2 = {
    # "name": "joy",
    "job": "DevOps",
    'id': '643'
}
response = requests.patch(api_url, user2)
new_user = response.json()
print(new_user)

print(response.json())
assert new_user["job"] == "DevOps"
