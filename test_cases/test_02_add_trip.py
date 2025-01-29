from base_pages.Add_Trips_Page import TripsPage
from base_pages.Login_Page import LoginPage
from utils.custom_logger import Log_Maker
from utils.read_config import Read_Config
from utils import generate_test_data
from utils import excel
import pytest
import time


class Test_03_WB_Add_Trip:
	data_sheet_path = Read_Config.get_data_sheet_file_path()
	attachment_image_path = Read_Config.get_attachment_file_path()
	username = excel.read_data(data_sheet_path,"Sheet1", 2,1)
	password = excel.read_data(data_sheet_path,"Sheet1", 2, 2)
	rows = excel.get_row_count(data_sheet_path,"Added_Trip_Data") + 1
	add_trip_form_title = "ADD VEHICLE'S REGISTRATION, LOAD AND JOURNEY DETAILS | PUNJAB AXLE LOAD DATA APPLICATION"
	previous_trip_page = "PREVIOUS ENTRIES | PUNJAB AXLE LOAD DATA APPLICATION"
	status_list = []
	logger = Log_Maker.log_gen()
#"""
	@pytest.mark.smoke
	@pytest.mark.AddAndVerifyTrip
	def test_add_new_trip(self, setup):
		self.driver = setup
		self.driver_name = generate_test_data.generate_fake_name()
		self.driver_CNIC = generate_test_data.generate_cnic()
		self.driver_phone = generate_test_data.generate_phone_no()
		self.vehicle_reg_no = generate_test_data.generate_vehicle_registration()
		self.vehicle_weight = generate_test_data.generate_weight()
		#def write_data(file,sheetname,row_num,column_num,data)
		excel.write_data(self.data_sheet_path, "Added_Trip_Data", self.rows, 1, self.driver_name)
		excel.write_data(self.data_sheet_path, "Added_Trip_Data", self.rows, 4, self.driver_CNIC)
		excel.write_data(self.data_sheet_path, "Added_Trip_Data", self.rows, 5, f"03{self.driver_phone}")
		excel.write_data(self.data_sheet_path, "Added_Trip_Data", self.rows, 2, self.vehicle_reg_no)
		excel.write_data(self.data_sheet_path, "Added_Trip_Data", self.rows, 3, self.vehicle_weight)
		
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
				
		self.AddTrip = TripsPage(self.driver)
		self.AddTrip.navigate_to_add_trip_form()
		time.sleep(4)
		assert self.driver.title == self.add_trip_form_title, "Title not matched"
		if self.driver.title != self.add_trip_form_title:
			self.status_list.append("Fail")
			self.logger.info("--->  Navigated to add trip form")
		else:
			self.status_list.append("Pass")
		
		self.logger.info("--->  Attempting to fill Add Trip form")
		self.AddTrip.enter_vehicle_registration_province()
		self.AddTrip.enter_reg_no(self.vehicle_reg_no)
		self.AddTrip.select_vehicle_type()
		self.AddTrip.select_unit_of_weight()
		self.AddTrip.enter_weight_value(self.vehicle_weight)
		self.AddTrip.select_origin_province()
		self.AddTrip.select_origin_district()
		self.AddTrip.select_destination_province()
		self.AddTrip.select_destination_district()
		self.AddTrip.enter_driver_name(self.driver_name)
		self.AddTrip.enter_driver_mobile_no(self.driver_phone)
		self.AddTrip.enter_driver_cnic(self.driver_CNIC)
		self.AddTrip.select_commodity()
		self.AddTrip.select_sub_commodity()
		self.logger.info("--->  Add Trip form was filled without attachments")
		self.AddTrip.upload_vehicle_front_picture(self.attachment_image_path)
		self.AddTrip.upload_reciept_picture(self.attachment_image_path)
		self.logger.info("--->  Add Trip form attachments added")
		self.AddTrip.click_save_trip_data()
		self.logger.info("--->  Add Trip from data saved")
		time.sleep(2)
		assert self.driver.title == self.previous_trip_page, "Title not matched"
		if self.driver.title != self.previous_trip_page:
			self.status_list.append("Fail")
		else:
			self.status_list.append("Pass")
		if "Fail" in self.status_list:
			assert False
		else:
			assert True
		print(self.status_list)
		self.driver.close()
#"""