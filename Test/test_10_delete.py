from testdata.delete_user import delete_user_url_data as dd , delete_user_url_code as dc
import allure


@allure.step('Delete Method Code')
def test_delete_user_response_code():
    assert dc  == 204


# @allure.step("Delete User Body")
# def test_delete_user_data():
#     assert dd == ''
