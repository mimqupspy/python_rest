from testdata.list_users import *
import allure


@allure.step('Test List User GET Method')
def test_list_resources():
    assert response_code == 200


@allure.step('Check First Name')
def test_first_name():
    assert data["data"][0]["first_name"] == "Michael"


@allure.step('Check First User Email')
def test_email():
    assert data["data"][0]["email"] == "michael.lawson@reqres.in"
