from testdata.put_user import put_user_url_code as pc ,put_user_url_data as pd
import allure


@allure.step('PUT Method Code')
def test_put_user_response_code():
    assert pc == 200


@allure.step('create user name check')
def test_put_user_data():
    assert pd["name"] == "adminuser" and pd["job"] == "Admin"
