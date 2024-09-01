from locators import Locators
from conftest import driver
import time
class TestRegistration:
    def test_incorrect_password(self, driver):
        driver.find_element(*Locators.button_login_main_page).click()
        driver.find_element(*Locators.button_register_1).click()
        driver.find_element(*Locators.input_name).send_keys('alexander_cheremisov')
        driver.find_element(*Locators.input_email).send_keys('alexander_cheremisov_13_99@mail.ru')
        driver.find_element(*Locators.input_password).send_keys('28')
        driver.find_element(*Locators.button_register_2).click()
        assert driver.find_element(*Locators.message_incorrect_password).text == 'Некорректный пароль'
        time.sleep(3)