
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://www.target.com/")
sleep(2)

@when("Click on cart icon")
def click_on_cart_icon(context):
    context.driver.find_element('.styles_cartIconDiv__jzkzP').click()

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS.SELECTOR, 'h1' ).text
    assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'


@when("Click on account icon")
def click_on_account_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '#account-sign-in').click()


@then("Click on 'Sign in or create account' button")
def click_on_account_button(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]').click()


@then("Verify Sign in form opened")
def sign_in_form(context):
    expected_result = 'Sign in or create account'
    actual_result = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in or create account')]").text
    assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'
