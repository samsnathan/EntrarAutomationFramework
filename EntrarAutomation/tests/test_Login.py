import pytest

from pageObjects import LoginPage
from pageObjects.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestHome(BaseTest):

    @pytest.mark.parametrize("user_name,password",ExcelUtils.get_data_from_excel("ExcelFiles/InputData.xlsx","LoginTest"))
    def test_login_click(self, user_name, password):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        main_page = login_page.login_to_application(user_name, password)
        assert main_page.display_status_of_school_name_on_main_page()
