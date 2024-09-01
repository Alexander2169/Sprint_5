from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from conftest import driver


class TestGoToSection:
    def test_go_to_the_buns_section(self, driver):
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.button_login_main_page))
        driver.find_element(*Locators.fillings_section).click()
        driver.find_element(*Locators.buns_section).click()
        assert driver.find_element(*Locators.selected_button).text == "Булки"


