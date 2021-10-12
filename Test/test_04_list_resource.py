from testdata.list_resource import list_resource_data, list_resource_response_code
import allure


@allure.step('list_resource_response_code')
def test_list_resource_response_code():
    assert list_resource_response_code == 200


@allure.step('list_resource_data not empty')
def test_list_resource_data_not_empty():
    assert list_resource_data is not {}


@allure.step('list_resource_data total pages')
def test_list_resource_data_total_pages():
    assert list_resource_data["total_pages"] == 2



