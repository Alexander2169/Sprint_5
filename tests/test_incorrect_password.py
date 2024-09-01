from locators import Locators
from conftest import driver
from data import UsersTestData
class TestRegistration:
    def test_incorrect_password(self, driver):
        driver.find_element(*Locators.button_login_main_page).click()
        driver.find_element(*Locators.button_register_1).click()
        driver.find_element(*Locators.input_name).send_keys(UsersTestData.username)
        driver.find_element(*Locators.input_email).send_keys(UsersTestData.email)
        driver.find_element(*Locators.input_password).send_keys('28')
        driver.find_element(*Locators.button_register_2).click()
        assert driver.find_element(*Locators.message_incorrect_password).text == 'Некорректный пароль'
