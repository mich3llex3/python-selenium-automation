from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
TOTAL_TXT = (By.XPATH, "//h2[./span[contains(text(), 'subtotal')]]")
CART_PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*TOTAL_TXT).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


#@then("Verify 'Your cart is empty' message is shown")
#def verify_cart_empty_msg(context):
 #   actual = context.driver.find_element(*CART_EMPTY_MSG).text
    expected = 'Your cart is empty'
  #  assert actual == expected, f'Expected {expected} did not match actual {actual}'


@then("Verify correct product is in cart")
def verify_product_name(context):
    actual_product = context.driver.find_element(*CART_PRODUCT_TITLE).text
    print("Product name in cart:", actual_product)
    assert actual_product[:25] == context.product_name[:25], f'Expected {context.product_name}, but got {actual_product}'