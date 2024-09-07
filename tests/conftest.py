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




