import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    wait= driver.webDaiverWait(driver, 10)
    driver.get("https://www.google.com/")
    driver.maximize_window()