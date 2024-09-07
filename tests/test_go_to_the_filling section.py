from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver

class TestGoToSection:
    def test_go_to_the_fillings_section(self, driver):
        driver.find_element(*Locators.sauces_section).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(Locators.button_login_main_page))
        driver.find_element(*Locators.fillings_section).click()
        assert driver.find_element(*Locators.selected_button).text == "Начинки"



