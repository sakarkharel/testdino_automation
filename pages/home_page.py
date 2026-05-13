from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class HomePage(BasePage):
    URL = "https://storedemo.testdino.com/"
    NAV_BAR_ABOUT_US = (By.CSS_SELECTOR, '[data-testid="header-menu-about-us"]')
    NAV_BAR_CONTACT_US = (By.CSS_SELECTOR, '[data-testid="header-menu-contact-us"]')
    NAV_BAR_ALL_PRODUCTS = (By.CSS_SELECTOR, '[data-testid="header-menu-all-products"]')
    SHOP_NOW = (By.CSS_SELECTOR, '[data-testid="hero-shop-now"]')
    WISH_LIST = (By.CSS_SELECTOR, '[data-testid="header-wishlist-icon"]')
    HEADER_ICON = (By.CSS_SELECTOR, '[data-testid="header-user-icon"]')
    CART_ICON = (By.CSS_SELECTOR, '[data-testid="header-cart-icon"]')
    CART_DRAWER = (By.CSS_SELECTOR, '[data-testid="cart-drawer"]')
    AUDIO_CAMERA = (By.CSS_SELECTOR, '[data-testid="category-title-camera"]')
    APPLIANCES = (By.CSS_SELECTOR, '[data-testid="category-title-appliances"]')
    GADGETS = (By.CSS_SELECTOR, '[data-testid="category-title-gadgets"]')
    PC_LAPTOPS = (By.CSS_SELECTOR, '[data-testid="category-title-laptop"]')
    LAPTOP_DISCOUNT = (By.CSS_SELECTOR, '[data-testid="offer-shop-now-1"]')
    WATCH_DISCOUNT = (By.CSS_SELECTOR, '[data-testid="offer-shop-now-2"]')
    CATEGORY_PRODUCT_SMARTPHONES = (By.CSS_SELECTOR, '[data-testid="offer-shop-now-2"]')
    Q_ONE  =   ( By.XPATH, "//summary[normalize-space()='What is TestDino Demo Store?']")
    ANSWER_ONE = (By.XPATH, "//div[contains(., 'TestDino Demo Store is a fully functional')]")
    Q_TWO = ( By.XPATH, "//summary[normalize-space()='Can I actually purchase products from this demo store?']")
    ANSWER_TWO = (By.XPATH, "//div[contains(., 'This is a demonstration website')]")
    Q_THREE = ( By.XPATH, "//summary[normalize-space()='What features does this demo e-commerce site include?']")
    ANSWER_THREE = (By.XPATH, "//div[contains(., 'Our demo store includes: product catalog')]")
    Q_FOUR = ( By.XPATH, "//summary[normalize-space()='Is this demo store mobile-friendly?']")
    ANSWER_FOUR = (By.XPATH, "//div[contains(., 'Yes! TestDino Demo Store is fully')]")
    Q_FIVE = ( By.XPATH, "//summary[normalize-space()='What technologies power this demo e-commerce website?']")
    ANSWER_FIVE = (By.XPATH, "//div[contains(., 'This demo store is built with React.js')]")
    Q_SIX = ( By.XPATH, "//summary[normalize-space()='How can I use this demo for testing?']")
    ANSWER_SIX = (By.XPATH, "//div[contains(., 'You can freely browse products')]")
    Q_SEVEN = ( By.XPATH, "//summary[normalize-space()='Does the demo store have real product data?']")
    ANSWER_SEVEN = (By.XPATH, "//div[contains(., 'Yes, we use realistic product data including')]")
    Q_EIGHT = ( By.XPATH, "//summary[normalize-space()='Is my data secure on this demo website?']")
    ANSWER_EIGHT = (By.XPATH, "//div[contains(., 'While this is a demo environment')]")


    def load(self):
        self.open(self.URL)
        self.wait_for_home_page()

    def wait_for_home_page(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.SHOP_NOW))
        
    def click_nav_bar_about_us(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NAV_BAR_ABOUT_US)
        ).click()
    
    def click_nav_bar_contact_us(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NAV_BAR_CONTACT_US)
        ).click()

    def click_nav_bar_all_products(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NAV_BAR_ALL_PRODUCTS)
        ).click()

    def click_nav_bar_to_wishlist(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.WISH_LIST)
        ).click()

    def click_nav_bar_to_header_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.HEADER_ICON)
        ).click()

    def click_nav_bar_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CART_DRAWER)
        )
    
    def click_shop_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SHOP_NOW)
        ).click()

    def click_audio_and_camera(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.AUDIO_CAMERA)
        ).click()

    def click_appliances(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.APPLIANCES)
        ).click()
    
    def click_gadgets(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.GADGETS)
        ).click()

    def click_pc_and_laptops(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PC_LAPTOPS)
        ).click()

    def click_laptop_discount(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LAPTOP_DISCOUNT)
        ).click()

    def click_watch_discount(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.WATCH_DISCOUNT)
        ).click()


    def click_faq_question_one(self):
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_speed=400
        # scroll_iteration=int(page_height/scroll_speed)

        for _ in range(10):
            self.driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.Q_ONE)
        ).click()

    
    def is_faq_answer_one_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ANSWER_ONE)
        ).is_displayed()
    

    ## faq two
    def click_faq_question_two(self):
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_speed=400

        for _ in range(10):
            self.driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.Q_TWO)
        ).click()

        
    def is_faq_answer_two_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ANSWER_TWO)
        ).is_displayed()
    

    ## faq three
    def click_faq_question_three(self):
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_speed=400

        for _ in range(10):
            self.driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.Q_THREE)
        ).click()

        
    def is_faq_answer_three_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ANSWER_THREE)
        ).is_displayed()
    
    ## faq fours 

    def click_faq_question_four(self):
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_speed=400

        for _ in range(10):
            self.driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.Q_FOUR)
        ).click()

        
    def is_faq_answer_four_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ANSWER_FOUR)
        ).is_displayed()
    
    ## faq five 

    def click_faq_question_five(self):
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_speed=400

        for _ in range(10):
            self.driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.Q_FIVE)
        ).click()

        
    def is_faq_answer_five_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ANSWER_FIVE)
        ).is_displayed()
    
    ## faq six 

    def click_faq_question_six(self):
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_speed=400

        for _ in range(10):
            self.driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.Q_SIX)
        ).click()

        
    def is_faq_answer_six_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ANSWER_SIX)
        ).is_displayed()
    
    ## faq seven 

    def click_faq_question_seven(self):
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_speed=400

        for _ in range(10):
            self.driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.Q_SEVEN)
        ).click()

        
    def is_faq_answer_seven_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ANSWER_SEVEN)
        ).is_displayed()
    
    ## faq eight 

    def click_faq_question_eight(self):
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_speed=400

        for _ in range(10):
            self.driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.Q_EIGHT)
        ).click()

        
    def is_faq_answer_eight_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ANSWER_EIGHT)
        ).is_displayed()
    
    
    
class Footer(BasePage):
    TWITTER_LINK = (By.CSS_SELECTOR, '[data-testid="footer-twitter-icon"]')
    LINKEDIN_LINK = (By.CSS_SELECTOR, '[data-testid="footer-linkedin-icon"]')
    GITHUB_LINK = (By.CSS_SELECTOR, '[data-testid="footer-github-icon"]')
    SHIPPING_POLICY = (By.CSS_SELECTOR, '[data-testid="footer-policy-shipping-policy"]')
    RETURN_POLICY = (By.CSS_SELECTOR, '[data-testid="footer-policy-return-policy"]')
    CANCEL_POLICY = (By.CSS_SELECTOR, '[data-testid="footer-policy-cancellation"]')
    FAQ = (By.CSS_SELECTOR, '[data-testid="footer-policy-faq"]')
    HOME = (By.CSS_SELECTOR, '[data-testid="footer-home"]')
    TESTDINO_LOGO = (By.CSS_SELECTOR, '[data-testid="footer-logo"]')
    ABOUT_US = (By.CSS_SELECTOR, '[data-testid="footer-about-us"]')
    CONTACT_US = (By.CSS_SELECTOR, '[data-testid="footer-contact-us"]')
    ALL_PRODUCTS = (By.CSS_SELECTOR, '[data-testid="footer-all-products"]')
    PRIVACY_POLCIY = (By.CSS_SELECTOR, '[data-testid="footer-privacy-policy"]')
    TERMS_OF_SERVICE = (By.CSS_SELECTOR, '[data-testid="footer-terms-of-service"]')

    
    def click_social_twitter(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TWITTER_LINK)
        ).click()


    def click_social_linkedin(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LINKEDIN_LINK)
        ).click()

    def click_social_github(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.GITHUB_LINK)
        ).click()

    def click_shipping_policy(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SHIPPING_POLICY)
        ).click()

    def click_return_policy(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.RETURN_POLICY)
        ).click()

    def click_cancel_policy(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CANCEL_POLICY)
        ).click()

    def click_faq(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FAQ)
        ).click()

    def click_testdino_logo(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TESTDINO_LOGO)
        ).click()

    def click_home(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.HOME)
        ).click()


    def click_about_us(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ABOUT_US)
        ).click()

    def click_contact_us(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTACT_US)
        ).click()

    def click_all_products(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ALL_PRODUCTS)
        ).click()

    def click_privacy_policy(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PRIVACY_POLCIY)
        ).click()

    def click_terms_of_service(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TERMS_OF_SERVICE)
        ).click()

    
    


    
