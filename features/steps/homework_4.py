from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open Target Circle page")
def open_target_circle_page(context):
    context.driver.get("https://www.target.com/circle")
    sleep(2)

@then("Verify Target Circle has two story cards")
def verify_story_cards(context):
   cards = context.driver.find_elements(By.CSS_SELECTOR, 'div[data-test]')
   assert len(cards) >= 2
   sleep(2)

@given("Open Target home page")
def open_target_circle_page(context):
    context.driver.get("https://www.target.com")

    sleep(5)

@then('Select product to add')
def select_product(context):
    sleep(5)

    product = context.driver.find_element(By.XPATH, "(//button[contains(text(), 'Add to cart')])[1]")
    context.driver.execute_script("arguments[0].click();", product)

    sleep(5)




