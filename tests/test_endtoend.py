
import pytest 
from pages.home_page import HomePage, Footer
from pages.login_page import LoginPage
from pages.signup_page import SignUp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


### EndtoEnd user process 

def test_end_to_end(driver):
    home=HomePage(driver)
    home.load()
    home.click_nav_bar_to_header_icon()
    assert "login" in driver.current_url

    signup_link = LoginPage(driver)
    signup_link.load()
    signup_link.click_on_signup_link()
    assert "signup" in driver.current_url


    insert_signup_credentials= SignUp(driver)
    insert_signup_credentials.load()
    insert_signup_credentials.click_signup_button("ankit", "khanal", "98hanal123@gmail.com", "K123!!!536")
    WebDriverWait(driver, 10).until(
        lambda driver: "login" in driver.current_url
    )
    assert "login" in driver.current_url


    insert_login_details=LoginPage(driver)
    insert_login_details.load()
    insert_login_details.login_with_valid_credentials("98hanal123@gmail.com", "K123!!!536")
    time.sleep(3)
    assert driver.current_url == "https://storedemo.testdino.com/"






