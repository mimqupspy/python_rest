from testdata.patch_user import patch_user_url_code as pc , patch_user_url_data as pd
import allure

@allure.step('PUT Method Code')
def test_patch_user_response_code():
    assert pc == 200


@allure.step('create user name check')
def test_patch_user_data():
    assert pd["name"] == "morpheus" and pd["job"] == "zion resident"
