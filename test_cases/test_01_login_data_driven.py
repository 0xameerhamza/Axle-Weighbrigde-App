import time
import  pytest
from utils import excel
from base_pages.Login_Page import LoginPage
from utils.custom_logger import Log_Maker
from utils.read_config import Read_Config

# """
class Test_02_WB_Login:
	data_sheet_path = Read_Config.get_data_sheet_file_path()
	status_list = []
	rows = excel.get_row_count(data_sheet_path,"Sheet1")
	first_execution_flag = True
	logger = Log_Maker.log_gen()
	
	@pytest.mark.DataDrivenLogin
	@pytest.mark.smoke
	def test_valid_login(self, setup):
		
		for row in range(2,self.rows+1):
			if not self.first_execution_flag:
				self.driver.refresh()
			else:
				self.driver = setup
			self.username = excel.read_data(self.data_sheet_path,"Sheet1", row,1)
			self.password = excel.read_data(self.data_sheet_path,"Sheet1", row, 2)
			self.expected_login_status = excel.read_data(self.data_sheet_path,"Sheet1", row,3)
			while True:
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
			if self.expected_login_status == "Success":
				if self.driver.title == "Dashboard | PUNJAB AXLE LOAD DATA APPLICATION":
					self.status_list.append("Pass")
					time.sleep(4)
					self.WB_login.click_Logout()
					print("WARNIN::: Log out successful")
				else:
					time.sleep(3)
					self.driver.save_screenshot(".\\screenshots\\test_login_issue.png")
					self.status_list.append("Fail")
			elif self.expected_login_status == "Invalid Username or Password":
				if "Invalid Username or Password" in self.driver.page_source:
					self.status_list.append("Pass")
				else:
					time.sleep(3)
					self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
					self.status_list.append("Fail")
			elif self.expected_login_status == "User Not Found":
				if "User Not Found" in self.driver.page_source:
					self.status_list.append("Pass")
				else:
					time.sleep(3)
					self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
					self.status_list.append("Fail")
			self.first_execution_flag = False
		self.driver.close()
		print(self.status_list)
		if "Fail" in self.status_list:
			assert False
		else:
			assert True
# """