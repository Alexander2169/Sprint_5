from locators import Locators
from conftest import driver
from helpers import get_sign_up_data
class TestRegistration:
    def test_incorrect_password(self, driver):
        name_data, email_data, password_data = get_sign_up_data()
        driver.find_element(*Locators.button_login_main_page).click()
        driver.find_element(*Locators.button_register_1).click()
        driver.find_element(*Locators.input_name).send_keys(name_data)
        driver.find_element(*Locators.input_email).send_keys(email_data)
        driver.find_element(*Locators.input_password).send_keys('28')
        driver.find_element(*Locators.button_register_2).click()
        assert driver.find_element(*Locators.message_incorrect_password).text == 'Некорректный пароль'
