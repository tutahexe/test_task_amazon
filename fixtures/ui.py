from fixtures.cart import CartHelper
from fixtures.item_details import ItemDetailsHelper
from fixtures.landing import LandingHelper


class UI:

    def __init__(self, wd):
        self.wd = wd
        self.landing = LandingHelper(self)
        self.cart = CartHelper(self)
        self.item_details = ItemDetailsHelper(self)

    def open_landing(self):
        self.wd.get("https://www.amazon.com/")

    def close(self):
        """"Closes Web driver"""
        self.wd.quit()