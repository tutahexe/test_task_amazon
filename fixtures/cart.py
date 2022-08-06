from selenium.webdriver.common.by import By


class CartHelper:
    def __init__(self, ui):
        self.ui = ui

    def get_item_in_cart(self):
        item_in_cart = self.ui.wd.find_element(By.CLASS_NAME, "a-truncate-full")
        return item_in_cart.get_attribute("textContent")