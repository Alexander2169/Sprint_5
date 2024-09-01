from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from conftest import driver
import time
class TestGoToSection:
    def test_go_to_the_buns_section(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.button_personal_account))
        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.input_email_login).send_keys('alexander_cheremisov_13_777@mail.ru')
        driver.find_element(*Locators.input_password_login).send_keys('281077')
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.buns_section))
        driver.find_element(*Locators.buns_section).click()
        assert driver.find_element(*Locators.selected_button).text == "Булки"
        time.sleep(3)

