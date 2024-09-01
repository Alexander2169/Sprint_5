import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from conftest import driver

class TestRegistration:
    # Регистрация аккаунта пользователя с валидными значениями инпутов
    def test_registration_new_account_success_submit(self, driver):
        driver.find_element(*Locators.button_login_main_page).click()
        driver.find_element(*Locators.button_register_1).click()
        driver.find_element(*Locators.input_name).send_keys('alexander_cheremisov')
        driver.find_element(*Locators.input_email).send_keys('alexander_cheremisov_13_9@mail.ru')
        driver.find_element(*Locators.input_password).send_keys('281077')
        driver.find_element(*Locators.button_register_2).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_register_2))
        assert driver.find_element(*Locators.button_register_2).is_displayed()



