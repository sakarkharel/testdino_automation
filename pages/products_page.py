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
    BUY_NOW = (By.CSS_SELECTOR, '[data-testid="buy-now-button"]')
    CHECKOUT_FIRST_NAME = (By.CSS_SELECTOR, '[data-testid="checkout-first-name-input"]')
    CHECKOUT_EMAIL = (By.CSS_SELECTOR, '[data-testid="checkout-email-input"]')
    CHECKOUT_CITY = (By.CSS_SELECTOR, '[data-testid="checkout-city-input"]')
    CHECKOUT_STATE = (By.CSS_SELECTOR, '[data-testid="checkout-state-input"]')
    CHECKOUT_STREET_ADDRESS = (By.CSS_SELECTOR, '[data-testid="checkout-street-input"]')
    CHECKOUT_ZIP_CODE = (By.CSS_SELECTOR, '[data-testid="checkout-zip-code-input"]')
    CHECKOUT_COUNTRY = (By.CSS_SELECTOR, '[data-testid="checkout-country-input"]')
    CHECKOUT_SAVE_ADDRESS_BUTTON = (By.CSS_SELECTOR, '[data-testid="checkout-save-address-button"]')
    CHECKOUT_CLICK_NET_BANKING =(By.CSS_SELECTOR, '[data-testid="checkout-netbanking-button"]')
    CHECKOUT_HDFC_BANK =  (By.CSS_SELECTOR, '[data-testid="checkout-netbanking-bank-logo-HDFC"]')
    CHECKOUT_PLACE_ORDER = (By.CSS_SELECTOR, '[data-testid="checkout-place-order-button"]')



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
        

    def click_buy_now(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BUY_NOW)
        ).click()

### this method will complete the checkout process 
    def complete_checkout_process(self, firstname, email, city, state, street, zipcode, country ):
        firstname_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_FIRST_NAME)
        )
        firstname_input.clear()
        firstname_input.send_keys(firstname)


        email_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_EMAIL)
        )
        email_input.clear()
        email_input.send_keys(email)


        city_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_CITY)
        )
        city_input.clear()
        city_input.send_keys(city)


        state_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_STATE)
        )
        state_input.clear()
        state_input.send_keys(state)


        street_address_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_STREET_ADDRESS)
        )
        street_address_input.clear()
        street_address_input.send_keys(street)

        zip_code_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_ZIP_CODE)
        )
        zip_code_input.clear()
        zip_code_input.send_keys(zipcode)


        country_input= WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_COUNTRY)
        )
        country_input.clear()
        country_input.send_keys(country)


        click_save_address = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_SAVE_ADDRESS_BUTTON)
        )
        click_save_address.click()

        click_net_banking = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_CLICK_NET_BANKING)
        )
        click_net_banking.click()

        click_hdfc_bank = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_HDFC_BANK)
        )
        click_hdfc_bank.click()

        click_place_order = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_PLACE_ORDER)
        )
        click_place_order.click()







