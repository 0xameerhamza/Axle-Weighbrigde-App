import pytest
import time

from utils.read_config import Read_Config
from utils import excel
from utils.custom_logger import Log_Maker

from base_pages.Login_Page import LoginPage
from base_pages.View_Trips_Page import ViewTrip


class Test_04_WB_Verify_Trip:
	data_sheet_path = Read_Config.get_data_sheet_file_path()
	logger = Log_Maker.log_gen()

	username = excel.read_data(data_sheet_path,"Sheet1", 2,1)
	password = excel.read_data(data_sheet_path,"Sheet1", 2, 2)
	rows = excel.get_row_count(data_sheet_path,"Added_Trip_Data")
	print("***************Number of rows", rows)
	#rows = rows_nmbr + 1
	driver_name = excel.read_data(data_sheet_path, "Added_Trip_Data", rows, 1)
	vehicle_reg_no = excel.read_data(data_sheet_path, "Added_Trip_Data", rows, 2)
	
	@pytest.mark.TripVerification
	@pytest.mark.AddAndVerifyTrip
	@pytest.mark.ViewOnlyTrip
	def test_verify_added_trip(self, setup):
		self.driver = setup
		self.logger.info("--->  Driver setup successfully")
		while True:
			self.WB_login = LoginPage(self.driver)
			self.WB_login.enter_username(self.username)
			self.WB_login.enter_password(self.password)
			self.WB_login.enter_captcha_text()
			self.WB_login.click_SignIn()
			time.sleep(2)
			if "Incorrect Captcha" in self.driver.page_source:
				print("WARNING::: Incorrect Captcha Attempting again")
				self.logger.info("---> Captcha was incorrect")
				continue
			break
		self.logger.info("--->  Login was successful")
		self.VerifyTrip = ViewTrip(self.driver)
		self.VerifyTrip.navigate_to_view_trip_page()
		self.logger.info("--->  Navigated to view trip page")
		self.VerifyTrip.search_trip_by_reg_no(self.vehicle_reg_no)
		
		print(self.VerifyTrip.get_driver_name())
		assert self.driver_name.lower() == self.VerifyTrip.get_driver_name().lower(), "Driver Name not matched"
		if self.driver_name.lower() == self.VerifyTrip.get_driver_name().lower():
			self.logger.info(f"--->  Driver Name matched successfully: {self.driver_name}")
		else:
			self.logger.info(f"--->  Driver Name did not match: {self.driver_name}")
		assert self.vehicle_reg_no == self.VerifyTrip.get_vehicle_reg_no(), "Vehicle Reg No not matched"
		if self.vehicle_reg_no == self.VerifyTrip.get_vehicle_reg_no():
			self.logger.info(f"--->  Vehicle Reg no matched successfully: {self.vehicle_reg_no}")
		else:
			self.logger.info(f"--->  Vehicle Reg no did not match: {self.vehicle_reg_no}")
		self.driver.close()