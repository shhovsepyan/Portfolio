from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#1)Declare driver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


#2) Navigate to python.org
driver.get("https://www.python.org/")
driver.maximize_window()

#3)Search 'bla bla' text and click on "Go" button
driver.find_element(By.ID, "id-search-field").send_keys("bla bla")
time.sleep(3)
driver.find_element(By.ID, "submit").click()
time.sleep(3)

#4)Print "No Results found"
print(driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/ul').text)


#5)Page's current URL and title
print(driver.current_url)
print(driver.title)

#6)Close driver
driver.close()








