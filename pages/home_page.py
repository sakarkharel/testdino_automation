from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://storedemo.testdino.com/"
    NAV_BAR_ABOUT_US = (By.CSS_SELECTOR, '[data-testid="header-menu-about-us"]')
    NAV_BAR_CONTACT_US = (By.CSS_SELECTOR, '[data-testid="header-menu-contact-us"]')
    NAV_BAR_ALL_PRODUCTS = (By.CSS_SELECTOR, '[data-testid="header-menu-all-products"]')
    SHOP_NOW = (By.CSS_SELECTOR, '[data-testid="hero-shop-now"]')
    WISH_LIST = (By.CSS_SELECTOR, '[data-testid="header-wishlist-icon"]')
    HEADER_ICON = (By.CSS_SELECTOR, '[data-testid="header-user-icon"]')
    CART_ICON = (By.CSS_SELECTOR, '[data-testid="header-cart-icon"]')
    CART_DRAWER = (By.CSS_SELECTOR, '[data-testid="cart-drawer"]')


    def load(self):
        self.open(self.URL)
        self.wait_for_home_page()

    def wait_for_home_page(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.SHOP_NOW))
        
    def click_nav_bar_about_us(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NAV_BAR_ABOUT_US)
        ).click()
    
    def click_nav_bar_contact_us(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NAV_BAR_CONTACT_US)
        ).click()

    def click_nav_bar_all_products(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NAV_BAR_ALL_PRODUCTS)
        ).click()

    def click_nav_bar_to_wishlist(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.WISH_LIST)
        ).click()

    def click_nav_bar_to_header_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.HEADER_ICON)
        ).click()

    def click_nav_bar_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CART_DRAWER)
        )
    
        

    