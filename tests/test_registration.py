import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver




class TestRegistration:
    # Регистрация аккаунта пользователя с валидными значениями инпутов
    def test_registration_new_account_success_submit(self, driver):
        driver.find_element(*TestLocators.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit))
        driver.find_element(*TestLocators.input_name).send_keys('alexander_cheremisov')
        driver.find_element(*TestLocators.input_email).send_keys('alexander_cheremisov_13_77777@mail.ru')
        driver.find_element(*TestLocators.input_password).send_keys('281077')
        driver.find_element(*TestLocators.button_submit).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.button_login))
        assert driver.find_element(*TestLocators.button_register).is_displayed()



