import time
from base_pages.Login_Page import LoginPage
from utils.read_config import Read_Config
import pytest
from utils.custom_logger import Log_Maker

"""

class Test_01_WB_Login:
    username = Read_Config.get_username()
    invalid_username = Read_Config.get_invalid_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()
    
	#@pytest.mark.SimpleLogin
    def test_load_login_page(self, setup):
        self.driver = setup
        actual_title = self.driver.title
        expected_title = "Login | PUNJAB AXLE LOAD DATA APPLICATION"
        if actual_title == expected_title:
            assert True
            self.driver.close()
            self.logger.info("--->  Login page loads successful")
        else:
            self.driver.quit()
            assert False


	#@pytest.mark.SimpleLogin
    def test_valid_login(self, setup):
        while True:
            self.driver = setup
            #self.driver.get(self.login_page_URL)
            self.WB_login = LoginPage(self.driver)
            self.WB_login.enter_username(self.username)
            self.WB_login.enter_password(self.password)
            self.WB_login.enter_captcha_text()
            self.WB_login.click_SignIn()
            time.sleep(2)
            if "Incorrect Captcha" in self.driver.page_source:
                print("WARNING::: Incorrect Captcha Attempting again")
                continue
            break
        if self.driver.title == "Dashboard | PUNJAB AXLE LOAD DATA APPLICATION":
            self.logger.info("--->  Valid Login Test is passed")
            assert True
            self.driver.close()
        else:
            time.sleep(3)
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.quit()
            assert False




	#@pytest.mark.SimpleLogin
    def test_invalid_login(self, setup):
        while True:
            self.driver = setup
            #self.driver.get(self.login_page_URL)
            self.WB_login = LoginPage(self.driver)
            self.WB_login.enter_username(self.invalid_username)
            self.WB_login.enter_password(self.password)
            self.WB_login.enter_captcha_text()
            self.WB_login.click_SignIn()
            time.sleep(2)
            if "Incorrect Captcha" in self.driver.page_source:
                print("WARNING::: Incorrect Captcha Attempting again")
                continue
            break
        if "User Not Found" in self.driver.page_source:
            self.logger.info("--->  Invalid Login Test is passed")
            assert True
            self.driver.close()
        else:
            time.sleep(3)
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.quit()
            assert False

"""
