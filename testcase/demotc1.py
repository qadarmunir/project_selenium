import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class demotc1():
    def demo_testcase1():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com")
        print(driver.title)
        driver.close()
        var=democt1()
        var.demo_testcase1()
