from locators import Locators
from conftest import driver
from data import UsersTestData
class TestEntrance:
    def test_login_to_password_recovery_form(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.button_recover_password).click()
        driver.find_element(*Locators.button_login_recover_password).click()
        driver.find_element(*Locators.input_email_login).send_keys(UsersTestData.password)
        driver.find_element(*Locators.input_password_login).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_login).click()
        assert driver.find_element(*Locators.button_login).is_displayed()
