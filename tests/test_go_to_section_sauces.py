from locators import Locators
from conftest import driver

class TestGoToSection:
    def test_go_to_the_sauces_section(self, driver):
        driver.find_element(*Locators.fillings_section).click()
        driver.find_element(*Locators.sauces_section).click()
        assert driver.find_element(*Locators.selected_button).text == "Соусы"
