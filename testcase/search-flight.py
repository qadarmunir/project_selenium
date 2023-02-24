import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class search_flight():
    def demosearch_flight():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com")
        driver.maximize_window()
        var= search_flight()
        var.demosearch_flight()
