from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')


#@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_msg(context):
    actual = context.driver.find_element(*CART_EMPTY_MSG).text
    expected = 'Your cart is empty'
    assert actual == expected, f'Expected {expected} did not match actual {actual}'
