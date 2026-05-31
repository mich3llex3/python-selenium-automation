from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_RESULT_COUNT_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADDED_TO_CART_TXT = (By.XPATH, "//*[text()='Added to cart']")


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn


@when('Store product name')
def store_product_name(context):
    context.wait.until(EC.visibility_of_element_located(SIDE_NAV_ADD_TO_CART_BTN))
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print("Name stored:", context.product_name)


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.wait.until(
        EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN),
        message='Add to Cart button from side navigation not visible'
    ).click()
    context.wait.until(
        EC.visibility_of_element_located(ADDED_TO_CART_TXT),
        message='Added to cart text not shown'
    )


@then("Verify search results for {product} shown")
def verify_search_results(context, product):
    actual_result = context.driver.find_element(*SEARCH_RESULT_COUNT_TEXT).text
    assert product in actual_result, f'Expected "{product}" not in actual "{actual_result}"'