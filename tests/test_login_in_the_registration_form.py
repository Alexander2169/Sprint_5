from locators import Locators
from conftest import driver
from helpers import get_sign_up_data

class TestEntrance:
    def test_login_in_the_registration_form(self, driver):
        name_data, email_data, password_data = get_sign_up_data()
        driver.find_element(*Locators.button_login_main_page).click()
        driver.find_element(*Locators.button_register_1).click()
        driver.find_element(*Locators.button_login_in_registration).click()
        driver.find_element(*Locators.input_email_login).send_keys(email_data)
        driver.find_element(*Locators.input_password_login).send_keys(password_data)
        driver.find_element(*Locators.button_login).click()
        assert driver.find_element(*Locators.button_login).is_displayed()

