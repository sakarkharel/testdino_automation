import pytest 
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


def test_nav_to_about_us(driver):
    home = HomePage(driver)
    home.load()
    home.click_nav_bar_about_us()
    assert "about" in driver.current_url.lower()

def test_nav_to_contact_us(driver):
    home= HomePage(driver)
    home.load()
    home.click_nav_bar_contact_us()
    assert "contact" in driver.current_url.lower()

def test_nav_to_all_products(driver):
    home=HomePage(driver)
    home.load()
    home.click_nav_bar_all_products()
    assert "products" in driver.current_url.lower()

def test_nav_to_wishlist(driver):
    home=HomePage(driver)
    home.load()
    home.click_nav_bar_to_wishlist()
    assert "wishlist" in driver.current_url.lower()

def test_nav_to_header(driver):
    home=HomePage(driver)
    home.load()
    home.click_nav_bar_to_header_icon()
    assert "login" in driver.current_url.lower()

def test_nav_to_cart(driver):
    home=HomePage(driver)
    home.load()
    home.click_nav_bar_to_cart()
    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(home.CART_DRAWER)
    )
def test_shop_now(driver):
    home=HomePage(driver)
    home.load()
    home.click_shop_button()
    assert "products" in driver.current_url.lower()

def test_audio_camera(driver):
    home=HomePage(driver)
    home.load()
    home.click_audio_and_camera()
    assert "products" in driver.current_url.lower()

def test_appliances(driver):
    home=HomePage(driver)
    home.load()
    home.click_appliances()
    assert "products" in driver.current_url.lower()

def test_gadgets(driver):
    home=HomePage(driver)
    home.load()
    home.click_gadgets()
    assert "products" in driver.current_url.lower()

def test_pc_laptops(driver):
    home=HomePage(driver)
    home.load()
    home.click_pc_and_laptops()
    assert "products" in driver.current_url.lower()

def test_laptop_discount(driver):
    home=HomePage(driver)
    home.load()
    home.click_laptop_discount()
    assert "products" in driver.current_url.lower()

def test_watch_discount(driver):
    home=HomePage(driver)
    home.load()
    home.click_watch_discount()
    assert "products" in driver.current_url.lower()


