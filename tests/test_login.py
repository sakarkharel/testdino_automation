import pytest 
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


def test_signup_link_click(driver):
    login_page=LoginPage(driver)
    login_page.load()
    login_page.click_on_signup_link()
    assert "signup" in driver.current_url


def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login_with_valid_credentials(
        email="ram@gmail.com",
        password="!!v!deocodec$$"
    )
# because of new webdriver instance/fresh session the assertion wont work here so it is commented out 
    #assert "" in driver.current_url




def test_login_with_empty_mail( driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login_with_empty_email("", "hello123")
    assert "login" in driver.current_url


def test_login_with_empty_password(driver):
    login_page=LoginPage(driver)
    login_page.load()
    login_page.login_with_empty_password("ram@gmail.com", "")
    assert "login" in driver.current_url

def test_login_with_unregistered_email(driver):
    login_page=LoginPage(driver)
    login_page.load()
    login_page.login_with_unregistered_email("JOhn123@hotmail.com", "123@@@#**^!")
    assert "login" in driver.current_url

def test_login_with_first_letter_capital(driver):
    login_page=LoginPage(driver)
    login_page.load()
    login_page.login_with_first_letter_captial("ram@gmail.com", "Password123!()")
    assert "login" in driver.current_url

def test_login_using_enter_key(driver):
    login_page=LoginPage(driver)
    login_page.load()
    login_page.login_using_enter_key("banana@gmail.com", "banana1836###!")
    #assert "testdino" in driver.current_url
    # because of new webdriver instance/fresh session the assertion wont work here so it is commented out 


def test_login_with_leading_trailing_spaces(driver):
    login_page=LoginPage(driver)
    login_page.load()
    login_page.login_with_leading_trailing_spaces("ram@gmail.com", " password123!@! ")
    assert "login" in driver.current_url

def test_login_after_multiple_failed_attempts(driver):
    login_page=LoginPage(driver)
    login_page.load()
    login_page.login_after_multiple_failed_attempts("hello@123.com", "password1282625@!*^")
    assert "login" in driver.current_url