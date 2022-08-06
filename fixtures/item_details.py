from selenium.webdriver.common.by import By


class ItemDetailsHelper:
    def __init__(self, ui):
        self.ui = ui

    def add_to_cart(self):
        add_to_cart = self.ui.wd.find_element(By.ID, "add-to-cart-button")
        add_to_cart.click()

    def added_confirmation_is_displayed(self):
        confirmation_image = self.ui.wd.find_element(By.ID, "add-to-cart-confirmation-image")
        assert confirmation_image.is_displayed()
