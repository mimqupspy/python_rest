from testdata.delayed import delayed_response_code
import allure

#  successful login
@allure.step('delayed response code')
def test_delayed_response_code():
    assert delayed_response_code  == 200


@allure.step('delayed response code')
def test_load_time():
    pass
