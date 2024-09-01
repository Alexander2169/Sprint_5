from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from conftest import driver


class TestRegistration:
    def test_registration(self, driver):
        driver.find_element(*Locators.button_login_main_page).click()
        driver.find_element(*Locators.button_register_1).click()
        driver.find_element(*Locators.input_name).send_keys('alexander_cheremisov')
        driver.find_element(*Locators.input_email).send_keys('alexander_cheremisov_13_582@mail.ru')
        driver.find_element(*Locators.input_password).send_keys('281077')
        driver.find_element(*Locators.button_register_2).click()
        assert driver.find_element(*Locators.button_register_2).is_displayed()




