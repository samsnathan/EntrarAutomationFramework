from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.MainPage import MainPage


class LoginPage(BasePage):

    user_name_field_id = "username"
    password_field_id = "password"
    login_button_id = "login-btn"

    def __init__(self, driver):
        self.driver = driver

    def enter_user_name(self,user_name_text):
        self.type_into_element(user_name_text,"user_name_field_id",self.user_name_field_id)

    def enter_password(self,password_text):
        self.type_into_element(password_text,"password_field_id",self.password_field_id)

    def click_on_login_button(self):
        self.element_click("login_button_id",self.login_button_id)
        return MainPage(self.driver)

    def login_to_application(self,user_name_text,password_text):
        self.enter_user_name(user_name_text)
        self.enter_password(password_text)
        return self.click_on_login_button()
