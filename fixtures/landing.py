from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class LandingHelper:
    def __init__(self, ui):
        self.ui = ui

    def search_for_item(self, text="software testing"):
        elem = self.ui.wd.find_element(By.ID, "twotabsearchtextbox")
        elem.clear()
        elem.send_keys(text)
        elem.send_keys(Keys.RETURN)

    def get_items_from_page(self):
        return self.ui.wd.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

    def get_first_item_title(self):
        first_item = self.ui.wd.find_element(By.XPATH, "//div[@data-component-type='s-search-result']")[0]
        return first_item.find_element(By.CLASS_NAME, "a-size-base-plus.a-color-base.a-text-normal").text

    def open_item(self, i=0):
        search_results = self.ui.wd.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
        search_results[i].click()

    def open_cart(self):
        cart = self.ui.wd.find_element(By.ID, "nav-cart-count")
        cart.click()
