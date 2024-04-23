import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.BasePage import BasePage
from pageObjects.LoginPage import LoginPage

class HomePage(BasePage):
    login_button_xpath = "//a[normalize-space()='Login']"

    def __init__(self, driver):
        super().__init__(driver)

    login_option_link_text = "Login"

    def click_on_login_button(self):
        self.element_click("login_button_xpath", self.login_button_xpath)

    def navigate_to_login_page(self):
        self.click_on_login_button()
        #time.sleep(5)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.ID, "login-btn")))
        return LoginPage(self.driver)
