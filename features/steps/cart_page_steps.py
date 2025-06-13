from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Open cart page')
def open_cart_page(context):
    print("Opening cart page...")
    context.driver.get('https://www.target.com/cart')

@then('Verify cart has correct product')
def verify_cart_product_name(context):
     product_name_in_cart = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text.strip()
     print('Name in cart:', product_name_in_cart)
     assert context.product_name in product_name_in_cart
     f'Expected context.product_name, not found in cart: "{product_name_in_cart}"'


@then('Verify cart has {amount} item')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]").text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    expected_text = 'Your cart is empty'
    assert actual_text == expected_text, f"Error, expected {expected_text} but got actual {actual_text}"