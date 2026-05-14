from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.home_page import HomePage
import re

class ProductPage(BasePage):

    URL = "https://storedemo.testdino.com/products"
    SEARCH_BAR = (By.CSS_SELECTOR, '[data-testid="all-products-search-input"]')
    RESULTS_TEXT = (By.CSS_SELECTOR, '[data-testid="all-products-results-count"]')
    LIST_VIEW_BTN = (By.CSS_SELECTOR, '[data-testid="all-products-view-switcher-list"]')
    GRID_VIEW_BTN = (By.CSS_SELECTOR, '[data-testid="all-products-view-switcher-grid"]')
    PRODUCT_CONTAINER = (By.CSS_SELECTOR, '[data-testid="products-container"]')
    FILTER_BUTTON = (By.CSS_SELECTOR, '[data-testid="all-products-filter-text"]')
    FILTER_CATEGORY = (By.CSS_SELECTOR, '[data-testid="all-products-category-select"]')
    MOUSE_TITLE = (By.XPATH, "//h2[@data-testid='all-products-header' and contains(., 'Mouse')]")


    def load(self):
        self.open(self.URL)
        self.wait_for_search_bar()
    
    def wait_for_search_bar(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.SEARCH_BAR)
        )

    def search_product(self, text):
        search = self.driver.find_element(*self.SEARCH_BAR)
        search.clear()
        search.send_keys(text)

    def get_results_count(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.RESULTS_TEXT)
        )

        text = element.text.strip()

        if "no products found" in text.lower():
            return 0

        match = re.search(r"(\d+)", text)
        if not match:
            raise AssertionError(f"Unexpected results text: {text}")

        return int(match.group(1))


    def search_and_assert_count(self, text, expected_count):
        self.search_product(text)

        actual_count = self.get_results_count()

        assert actual_count == expected_count, (
            f"Expected {expected_count} products, but got {actual_count}"
        )

    def switch_to_list_view(self):
        self.driver.find_element(*self.LIST_VIEW_BTN).click()

        # WebDriverWait(self.driver, 10).until(
        #     lambda d: "list" in d.find_element(*self.PRODUCT_CONTAINER).get_attribute("class").lower()
        # )

    # def assert_list_view_active(self):
    #     container = self.driver.find_element(*self.PRODUCT_CONTAINER)
    #     class_value = container.get_attribute("class").lower()

    #     assert "list" in class_value, f"Expected list view but got: {class_value}"

    def click_filter_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FILTER_BUTTON)
        ).click()

    def assert_filter_visible(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FILTER_CATEGORY)
        )

    def click_mouse(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MOUSE_TITLE)
        ).click()

    






