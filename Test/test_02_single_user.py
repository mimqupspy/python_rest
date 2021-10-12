from testdata.list_users import single_user_response_code, single_user_data
import allure


@allure.step('single_user_response_code')
def test_single_user_response_code():
    assert single_user_response_code == 200


@allure.step('single_user_email')
def test_single_user_email():
    assert single_user_data["data"]["email"] == "janet.weaver@reqres.in"


@allure.step('single_user_first_name')
def test_single_user_first_name():
    assert single_user_data["data"]["first_name"] == "Janet"
