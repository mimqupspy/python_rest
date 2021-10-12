from testdata.list_resource import single_resource_not_found_code,single_resource_not_found_data
import allure


@allure.step('single_resource_not_found_code')
def test_single_resoce_not_found_code():
    assert single_resource_not_found_code == 404


@allure.step('single_resource_response data not empty')
def test_single_resource_not_found():
    assert single_resource_not_found_data == {}
