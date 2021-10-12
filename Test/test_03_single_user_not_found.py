from testdata.list_users import single_user_not_found_response_code, single_user_not_found_data
import allure


@allure.step('single_user_not_found_response_code')
def test_single_user_not_found_response_code():
    assert single_user_not_found_response_code == 404


@allure.step('single_user_not_found_data')
def test_single_user_not_found_data():
    assert single_user_not_found_data == {}
