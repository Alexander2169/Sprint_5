from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from conftest import driver
import time

class TestRegistration:
    def test_registration(self, driver):
        driver.find_element(*Locators.button_login_main_page).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.button_register_1))
        driver.find_element(*Locators.button_register_1).click()
        driver.find_element(*Locators.input_name).send_keys('alexander_cheremisov')
        driver.find_element(*Locators.input_email).send_keys('alexander_cheremisov_13_358@mail.ru')
        driver.find_element(*Locators.input_password).send_keys('281077')
        driver.find_element(*Locators.button_register_2).click()
        assert driver.find_element(*Locators.button_register_2).is_displayed()
        time.sleep(5)



