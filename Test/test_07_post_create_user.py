from testdata.create_user import create_user_url_code, create_user_url_data
import allure


@allure.step('Post User Create Code')
def test_create_user_response_code():
    assert create_user_url_code == 201


@allure.step('create user name check')
def test_single_resource_not_found():
    assert create_user_url_data["name"] == "demouser"
