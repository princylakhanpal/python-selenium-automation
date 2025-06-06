from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

driver.find_element(By.ID,'search').send_keys('icecream')
driver.find_element(By.XPATH,"//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)
expected_text = 'icecream'
Verify search worked
Error,expected 'tea' not in actual {actual_text}"
print('test case passed')
driver.quit()

