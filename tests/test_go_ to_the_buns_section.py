from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from conftest import driver

class TestGoToSection:
    def test_go_to_the_buns_section(self, driver):
        driver.find_element(*Locators.fillings_section).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(Locators.selected_button))
        driver.find_element(*Locators.buns_section).click()
        assert driver.find_element(*Locators.selected_button).text == "Булки"




