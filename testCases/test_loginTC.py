import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from TestData.LoginPageData import LoginPageData
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLoginGh(BaseClass):

    def test_one(self, get_data):
        log = self.get_logger()
        login_page = LoginPage(self.driver)
        login_page.sign_in_button_m().click()
        self.verify_username_displayed()
        log.info("Entering Username")
        login_page.user_name_m().send_keys(get_data["username"])
        log.info("Entering Password")
        login_page.pass_word_m().send_keys(get_data["password"])
        login_page.submit_m().click()
        expected_title = self.driver.title
        assert expected_title=="GitHub"

    @pytest.fixture(params=LoginPageData.test_login_page_data)
    def get_data(self,request):
        return request.param
