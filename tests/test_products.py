import pytest
from pages.products_page import ProductPage


def test_search_item(driver):
    product_page = ProductPage(driver)
    product_page.load()
    product_page.search_and_assert_count("hard drive", 1)

def test_list_view(driver):
    page = ProductPage(driver)
    page.load()
    page.switch_to_list_view()
    # page.assert_list_view_active()

def test_filter_button(driver):
    product_page = ProductPage(driver)
    product_page.load()
    product_page.click_filter_button()
    product_page.assert_filter_visible()

def test_mouse_click(driver):
    product_page = ProductPage(driver)
    product_page.load()
    product_page.click_mouse()
    assert "logitech-mx" in driver.current_url.lower()


