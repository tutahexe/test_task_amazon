from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from models.item import Item


class LandingHelper:
    def __init__(self, ui):
        self.ui = ui

    def search_for_item(self, text=""):
        elem = self.ui.wd.find_element(By.ID, "twotabsearchtextbox")
        elem.clear()
        elem.send_keys(text)
        elem.send_keys(Keys.RETURN)

    def get_items_from_page(self):
        return self.ui.wd.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

    def build_item_objects_from_search_results(self, search_results):
        items = []
        for search_result in search_results:
            try:
                item_name = search_result.find_element(By.CLASS_NAME,
                                                       "a-size-base-plus.a-color-base.a-text-normal").text
            except NoSuchElementException:
                continue
            try:
                item_rate = search_result.find_element(By.CLASS_NAME, "a-icon-alt").get_attribute("textContent")
                item_rate_2 = str(item_rate)
                item_rate_3 = item_rate_2[0:3]
            except NoSuchElementException:
                continue
            try:
                item_date = search_result.find_element(By.CLASS_NAME,
                                                       "a-size-base.a-color-secondary.a-text-normal").get_attribute(
                    "textContent")
            except NoSuchElementException:
                item_date = "Aug 1, 0001"
            items.append(Item(item_name, item_rate_3, item_date))
            return items

    def get_first_item_title(self):
        first_item = self.ui.wd.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")[0]
        return first_item.find_element(By.CLASS_NAME, "a-size-base-plus.a-color-base.a-text-normal").text

    def open_item(self, i=0):
        search_results = self.ui.wd.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
        search_results[i].click()

    def open_cart(self):
        cart = self.ui.wd.find_element(By.ID, "nav-cart-count")
        cart.click()
