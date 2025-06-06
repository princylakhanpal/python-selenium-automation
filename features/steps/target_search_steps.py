from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@then('Verify search worked')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert 'tea' in actual_text, f"Error, expected 'tea' not in actual {actual_text}"

@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartIcon"]').click()
    sleep(5)

@then('Verify cart is empty')
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, 'h1[class*="styles_ndsHeading"]').text
    assert 'Your cart is empty' in actual_text, f"Error, expected 'Your cart is empty' in actual {actual_text}"

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