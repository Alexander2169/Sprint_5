from locators import Locators
from conftest import driver

class TestEntrance:
    def test_login_in_the_registration_form(self, driver):
        driver.find_element(*Locators.button_login_main_page).click()
        driver.find_element(*Locators.button_register_1).click()
        driver.find_element(*Locators.button_login_in_registration).click()
        driver.find_element(*Locators.input_email_login).send_keys('alexander_cheremisov_13_777@mail.ru')
        driver.find_element(*Locators.input_password_login).send_keys('281077')
        driver.find_element(*Locators.button_login).click()
        assert driver.find_element(*Locators.button_login).is_displayed()

