import pytest
from selenium import webdriver
from config import BASE_URL
@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.button_login_main_page).click()
    driver.find_element(*Locators.input_email_login).send_keys(UsersTestData.email)
    driver.find_element(*Locators.input_password_login).send_keys(UsersTestData.password)
    driver.find_element(*Locators.button_login).click()


