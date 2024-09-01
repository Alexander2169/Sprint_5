from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from conftest import driver

class TestEntrance:
    def test_login_to_password_recovery_form(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.button_recover_password))
        driver.find_element(*Locators.button_recover_password).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.button_login_recover_password))
        driver.find_element(*Locators.button_login_recover_password).click()
        driver.find_element(*Locators.input_email_login).send_keys('alexander_cheremisov_13_777@mail.ru')
        driver.find_element(*Locators.input_password_login).send_keys('281077')
        driver.find_element(*Locators.button_login).click()
        assert driver.find_element(*Locators.button_login).is_displayed()
