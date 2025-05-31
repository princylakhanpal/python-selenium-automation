
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
driver.get('https://www.amazon.com/')
driver.refresh()
sleep(10)

#Locators:
#Amazon logo, search by XPATH
driver.find_element(By.XPATH,"//i[@aria-label='Amazon']")

#Email field,search by ID
driver.find_element(By.ID,"ap_email_login")

#Continue button,search by XPATH
driver.find_element(By.XPATH,"//input[@class='a-button-input']")

#Conditions of use link,search by text
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")

#Privacy notice link,search by text
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")

#Need help link,search by XPATH
driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/account-issues/ref=unified_claim_collection?ie=UTF8']")

#Forgot your password link,search by XPATH
driver.find_element(By.XPATH,"//option[@name='I forgot my password']")

#Password reset page link,search by text
driver.find_element(By.XPATH,"//a[text()='Password reset page']")

#Create account page link,search by text
driver.find_element(By.XPATH,"//a[text()='Create Account page']")

#Create account button,search by XPATH
driver.find_element(By.XPATH,"//a[@class='a-link-normal']")








