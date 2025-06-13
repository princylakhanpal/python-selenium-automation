from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(By.ID, 'search').send_keys(search_word)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()
    sleep(2)

@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'] h4").text
    print('Product name stored: ', context.product_name)


@when('Confirm add to Cart button from side navigation bar')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_contentWrapper'] button[id*='addToCartButton']").click()
