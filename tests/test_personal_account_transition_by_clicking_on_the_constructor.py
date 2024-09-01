from locators import Locators
from conftest import driver
from data import UsersTestData

class TestNavigateToConstructor:
    def test_personal_account_transition_by_clicking_on_the_constructor(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.input_email_login).send_keys(UsersTestData.email)
        driver.find_element(*Locators.input_password_login).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_login).click()
        driver.find_element(*Locators.button_constructor_main_page).click()
        assert driver.find_element(*Locators.button_constructor_main_page).is_displayed()
