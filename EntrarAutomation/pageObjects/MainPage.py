from pageObjects.BasePage import BasePage


class MainPage(BasePage):
    #// span[normalize - space() = 'Dashboard']
    school_name_xpath = "//h4[normalize-space()='DELHI PUBLIC SCHOOL - BANGALORE EAST']"

    def display_status_of_school_name_on_main_page(self):
        return self.check_display_status_of_element("school_name_xpath",self.school_name_xpath)