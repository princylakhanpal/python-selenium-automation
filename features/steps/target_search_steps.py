from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@when('Click on Account')
def click_account_button(context):
    context.driver.find_element(By.CSS_SELECTOR, '#account-sign-in').click()
sleep(5)

@when('Click Sign in button')
def click_sign_in_button(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]').click()
sleep(5)

@then('Verify Sign in page opened')
def verify_sign_in_page_open(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '[class*="styles_ndsHeading"]').text
    assert 'Sign in or create account' in actual_text, f"Error, expected 'Sign in or create account' in actual {actual_text}"