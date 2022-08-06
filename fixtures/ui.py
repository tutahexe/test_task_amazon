from fixtures.cart import CartHelper
from fixtures.landing import LandingHelper


class Application:

    def __init__(self, wd, browser):
        self.wd = wd
        self.browser = browser
        self.landing = LandingHelper(self)
        self.cart = CartHelper(self)
