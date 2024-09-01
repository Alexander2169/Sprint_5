from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from conftest import driver


class TestNavigateToConstructor:
    def test_personal_account_transition_by_clicking_on_the_constructor(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.input_email_login).send_keys('alexander_cheremisov_13_777@mail.ru')
        driver.find_element(*Locators.input_password_login).send_keys('281077')
        driver.find_element(*Locators.button_login).click()
        driver.find_element(*Locators.button_constructor_main_page).click()
        assert driver.find_element(*Locators.button_constructor_main_page).is_displayed()
