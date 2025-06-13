from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']").click()
    # context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()



@then('Verify search worked for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert product in actual_text, f"Error, expected {product} not in actual {actual_text}"
