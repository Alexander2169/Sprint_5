from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from conftest import driver
from helpers import get_sign_up_data

class TestLogout:
    def test_logout(self, driver):
        name_data, email_data, password_data = get_sign_up_data()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.button_personal_account)).click()
        driver.find_element(*Locators.input_email_login).send_keys(email_data)
        driver.find_element(*Locators.input_password_login).send_keys(password_data)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.button_login))
        assert driver.find_element(*Locators.button_login).is_displayed()



