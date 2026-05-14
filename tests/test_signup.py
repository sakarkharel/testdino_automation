import pytest
from pages.signup_page import SignUp
import pytest 
from pages.home_page import HomePage, Footer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import random
import string
import uuid


@pytest.mark.parametrize(
    "first_name, last_name, email_add, password, expected_errors",
    [
        (
            "", "", "", "",
            [
                "First name is required",
                "Last name is required",
                "Email is required",
                "Password is required"
            ]
        ),
        (
            "John", "", "john@test.com", "Password123",
            [
                "Last name is required"
            ]
        ),
        (
            "", "Doe", "john@test.com", "Password123",
            [
                "First name is required"
            ]
        ),
        (
            "John", "Doe", "", "Password123",
            [
                "Email is required"
            ]
        ),
        (
            "John", "Doe", "invalid-email", "Password123",
            [
                "Email is invalid"
            ]
        ),
        (
            "John", "Doe", "john@test.com", "",
            [
                "Password is required"
            ]
        ),
    ]
)

def test_signup_validation_errors(
    driver,
    first_name,
    last_name,
    email_add,
    password,
    expected_errors
):
    signup_page = SignUp(driver)

    signup_page.load()

    signup_page.click_signup_button(
        first_name,
        last_name,
        email_add,
        password
    )

    actual_errors = signup_page.get_validation_errors()

    for error in expected_errors:
        assert error in actual_errors



def test_successful_signup(driver):
    signup_page = SignUp(driver)
    signup_page.load()

    first_name = random.choice(["John", "Jane", "Michael", "Emily", "Chris", "Sarah"])
    last_name = random.choice(["Doe", "Smith", "Johnson", "Brown", "Taylor", "Wilson"])

    email = f"{first_name.lower()}.{last_name.lower()}{uuid.uuid4().hex[:6]}@gmail.com"

    password = ''.join(random.choices(
        string.ascii_letters + string.digits,
        k=10
    ))

    signup_page.click_signup_button(
        first_name,
        last_name,
        email,
        password
    )
    print("CURRENT URL:", driver.current_url)
    time.sleep(10)
    assert "login" in driver.current_url


