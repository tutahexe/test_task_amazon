from fixtures.cart import CartHelper
from fixtures.item_details import ItemDetailsHelper
from fixtures.landing import LandingHelper


class Application:

    def __init__(self, wd, browser):
        self.wd = wd
        self.browser = browser
        self.landing = LandingHelper(self)
        self.cart = CartHelper(self)
        self.item_details = ItemDetailsHelper(self)

    def open_landing(self):
        self.wd.get("https://www.amazon.com/")
