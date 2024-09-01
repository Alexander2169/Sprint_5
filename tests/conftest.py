import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.button_login_in_main).click()
    driver.find_element(*Locators.input_email_login).send_keys('alexander_cheremisov_13_777@mail.ru')
    driver.find_element(*Locators.input_password_login).send_keys('281077')
    driver.find_element(*Locators.button_login).click()


