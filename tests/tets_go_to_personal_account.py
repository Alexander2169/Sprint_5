from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from conftest import driver
from conftest import login
import time

class TestGoToPersonalAccount:
    def test_go_to_personal_account(self, driver, login):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.profile))
        assert driver.find_element(*Locators.order_history).is_displayed()
        time.sleep(5)