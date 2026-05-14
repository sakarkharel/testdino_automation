from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.home_page import HomePage


class ContactUs(HomePage ):

    URL =  "https://storedemo.testdino.com/contact-us"
    FIRST_NAME = (By.CSS_SELECTOR, '[data-testid="contact-us-first-name-input"]')
    LAST_NAME = (By.CSS_SELECTOR, '[data-testid="contact-us-last-name-input"]')
    SUBJECT = (By.CSS_SELECTOR, '[data-testid="contact-us-subject-input"]')
    MESSAGE = (By.CSS_SELECTOR, '[data-testid="contact-us-message-input"]')
    SEND_BUTTON = (By.CSS_SELECTOR, '[data-testid="contact-us-submit-button"]')


    def load(self):
        self.open(self.URL)
        self.wait_for_contact_page()
    
    def wait_for_contact_page(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.SEND_BUTTON)
        )

    def fill_form(self, first_name="", last_name="", subject="", message=""):

        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.SUBJECT, subject)
        self.type(self.MESSAGE, message)

    def submit(self):
        self.click(self.SEND_BUTTON)

    def submit_contact_form(self, first_name, last_name, subject, message):
        self.fill_form(first_name, last_name, subject, message)
        self.submit()

    def get_validation_errors(self):
        return self.driver.find_elements(By.CLASS_NAME, "error")



