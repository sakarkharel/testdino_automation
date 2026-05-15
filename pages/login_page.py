from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.home_page import HomePage
import re


class LoginPage(BasePage):
    URL = "https://storedemo.testdino.com/login"
    SIGNUP_LINK = (By.CSS_SELECTOR, '[data-testid="login-signup-link"]')
    EMAIL_ADD_INPUT = (By.CSS_SELECTOR, '[data-testid="login-email-input"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="login-password-input"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="login-submit-button"]')

    def load(self):
        self.open(self.URL)
        self.wait_for_signup_link()
    
    def wait_for_signup_link(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.SIGNUP_LINK)
        )
    
    ## make methods independently 
    ## and then class EndtoEnd in the home_page.py 

    def enter_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL_ADD_INPUT)
        )
        email_input.clear()
        email_input.send_keys(email)


    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(password)
    
    def click_login_button(self):
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_btn.click()

    # the test cases i think 

    def login_with_valid_credentials(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    
    







       
    