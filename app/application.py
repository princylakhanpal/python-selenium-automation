

from pages.base_page import Page
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import Cartpage
from pages.sign_in_page import SignInPage
from pages.side_navigation_cart import SideNavigationCart


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = Cartpage(driver)
        self.sign_in_page = SignInPage(driver)
        self.side_navigation_cart = SideNavigationCart(driver)