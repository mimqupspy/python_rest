from testdata.list_resource import single_resource_response_code as srrc,single_resource_data
import allure


@allure.step('single_resource_response code')
def test_single_resource_response_code():
    assert srrc == 200


@allure.step('single_resource_response data not empty')
def test_single_resource_data_not_empty():
    assert single_resource_data is not {}


@allure.step('color is in resource data')
def test_color_is_in_resource_data():
    assert "color" in single_resource_data["data"]