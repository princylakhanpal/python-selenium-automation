from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


ACCOUNT_BTN = (By.CSS_SELECTOR, '[id="account-sign-in"]')
SIGN_IN_BTN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')

@when('Click on Account')
def click_account_button(context):
    context.driver.wait.until(EC.element_to_be_clickable(ACCOUNT_BTN)).click()


@when('Click Sign in button')
def click_sign_in_button(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN)).click()

@then('Verify Sign in page opened')
def verify_sign_in_page_open(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '[class*="styles_ndsHeading"]').text
    assert 'Sign in or create account' in actual_text, f"Error, expected 'Sign in or create account' in actual {actual_text}"