from locators import Locators
from conftest import driver
from data import UsersTestData
class TestEntrance:
    def test_login_to_your_personal_account(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.input_email_login).send_keys(UsersTestData.email)
        driver.find_element(*Locators.input_password_login).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_login).click()
        assert driver.find_element(*Locators.button_login).is_displayed()

