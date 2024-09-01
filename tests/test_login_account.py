from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from conftest import driver
import time

class TestEntrance:
    def test_login_account(self, driver):
        driver.find_element(*Locators.button_login_main_page).click()
        driver.find_element(*Locators.input_email_login).send_keys('alexander_cheremisov_13_777@mail.ru')
        driver.find_element(*Locators.input_password_login).send_keys('281077')
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.button_login))
        assert driver.find_element(*Locators.button_login).is_displayed()
        time.sleep(3)
