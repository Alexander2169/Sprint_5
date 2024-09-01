from locators import Locators
from conftest import driver
from data import UsersTestData
class TestRegistration:
    def test_registration(self, driver):
        driver.find_element(*Locators.button_login_main_page).click()
        driver.find_element(*Locators.button_register_1).click()
        driver.find_element(*Locators.input_name).send_keys(UsersTestData.username)
        driver.find_element(*Locators.input_email).send_keys(UsersTestData.email)
        driver.find_element(*Locators.input_password).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_register_2).click()
        assert driver.find_element(*Locators.button_register_2).is_displayed()




