import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class search_flight():
    def demosearch_flight():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()

      #going from
        going_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        going_from.click()
        going_from.send_keys("New York")
        going_from.send_keys(Keys.ENTER)

      #goging to
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.click()
        going_to.send_keys("London")
        going_to.send_keys(Keys.ENTER)

        #list of fligths
        list_of_flights = driver.find_element(By.XPATH, "//div[@class='flight-list']")
        print(len(list_of_flights))

        #selecting the first flight , so we use loop
        for i in list_of_flights:
            print(i.text)
            if i.text == "London":
                i.click()
                break

         #selecting the date
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']")).click()

            driver.find_element(By.XPATH, "//td[@id='22/03/2023']").click()
            driver.find_element(By.XPATH, "//body/div/div[@id='themeSnipe']/section/div/div/div/section/div/div[@id='booking_engine_modues']/div[@type='flights']/div[@id='BE_flight_form_wrapper']/div/div/div[1]/input[1]").click()




var= search_flight()
var.demosearch_flight()
