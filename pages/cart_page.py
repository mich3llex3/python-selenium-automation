from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    EMPTY_CART_MESSAGE = (By.XPATH,"//*[contains(text(),'Your cart is empty')]")
    def verify_empty_cart_message(self):
        return self.find_element(*self.EMPTY_CART_MESSAGE).is_displayed()