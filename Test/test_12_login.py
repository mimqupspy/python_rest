from testdata.login import login_url_code as lc,login_url_data as ld,un_login_url_code as ulc,un_login_url_data as uld
import allure

#  successful login
@allure.step('test_sucessfull_register_code')
def test_login_response_code():
    assert lc  == 200

@allure.step('test_sucessfull_login_token')
def test_login_sucessfull_token():
    assert ld["token"] is not ''


# unsuccessful login
@allure.step('test_unsucessfull_response_code')
def test_unsucessfull_login_code():
    assert ulc  == 400


@allure.step('test_unsucessfull_message')
def test_unsucessfull_message():
    assert uld['error'] == 'Missing password'
