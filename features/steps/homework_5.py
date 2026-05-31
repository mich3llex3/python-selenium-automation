from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@given("Open Target Circle page")
def open_target_circle_page(context):
    context.driver.get("https://www.target.com/circle")
    context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-test]')))

@then("Verify Target Circle has two story cards")
def verify_story_cards(context):
   cards = context.driver.find_elements(By.CSS_SELECTOR, 'div[data-test]')
   assert len(cards) >= 2

@given("Open Target home page")
def open_target_circle_page(context):
    context.driver.get("https://www.target.com")
    context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-test]')))

@then('Select product to add')
def select_product(context):
    context.wait.until(EC.element_to_be_clickable(By.XPATH, "(//button[contains(text(), 'Add to cart')])[1]"))

    product = context.driver.find_element(By.XPATH, "(//button[contains(text(), 'Add to cart')])[1]")
    context.driver.execute_script("arguments[0].click();", product)

    sleep(5)

@given ("Open blouse product page")
def open_blouse_product_page(context):
    context.driver.get("https://www.target.com/p/women-s-smocked-blouse-universal-thread-red/-/A-95081560?preselect=95162150#lnk=sametab")
@then ("Verify all colors can be selected")
def verify_colors(context):
    colors = context.driver.find_elements(By.CSS_SELECTOR, 'button[aria-label*="Color"]')

    for color in colors:
        context.driver.execute_script("arguments[0].click();", color)
        assert "Color" in color.get_attribute("aria-label")