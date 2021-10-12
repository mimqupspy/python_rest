from testdata.register import un_register_url_data as und, un_register_url_code as urc, register_url_data as rd,register_url_code as rc
import allure


@allure.step('test_sucessfull_register_code')
def test_sucessfull_response_code():
    assert rc  == 200

@allure.step('test_sucessfull_register_message')
def test_sucessfull_data():
    assert rd["token"] is not ''



@allure.step('test_unsucessfull_register_code')
def test_unsucessfull_response_code():
    assert urc  == 400


@allure.step('test_unsucessfull_message')
def test_unsucessfull_message():
    assert und['error'] == 'Missing password'
