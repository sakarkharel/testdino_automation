from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.home_page import HomePage



class SignUp(LoginPage):

    URL = "https://storedemo.testdino.com/signup"
    SIGNUP_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[data-testid="signup-submit-button"]')
    FIRST_NAME = (By.CSS_SELECTOR, '[data-testid="signup-firstname-input"]')
    LAST_NAME = (By.CSS_SELECTOR, '[data-testid="signup-lastname-input"]')
    EMAIL_ADD = (By.CSS_SELECTOR, '[data-testid="signup-email-input"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-testid="signup-password-input"]')
    ERROR_MESSAGES = (
        By.CLASS_NAME,
        "error"
    )

    def load(self):
        self.open(self.URL)
        self.wait_for_signup_submit_button()
    
    def wait_for_signup_submit_button(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.SIGNUP_SUBMIT_BUTTON)
        )
    

## just liek contact us yesma chai 
    def fill_form(self, first_name = "", last_name="", email_add="", password=""):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.EMAIL_ADD, email_add)
        self.type(self.PASSWORD, password)
        print("DEBUG EMAIL:", email_add)

    def submit(self):
        # self.click(self.SIGNUP_SUBMIT_BUTTON)
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.SIGNUP_SUBMIT_BUTTON) ).click()

    def click_signup_button(self, first_name, last_name, email_add, password):
        self.fill_form(first_name, last_name, email_add, password)
        self.submit()
   
    def get_validation_errors(self, timeout=5):

        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(
                self.ERROR_MESSAGES
            )
        )

        errors = self.driver.find_elements(
            *self.ERROR_MESSAGES
        )

        return [error.text for error in errors]




