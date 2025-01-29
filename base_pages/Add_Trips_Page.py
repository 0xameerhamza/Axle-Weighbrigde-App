import time
from utils.custom_logger import Log_Maker
# from utils import generate_test_data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TripsPage:
	logger = Log_Maker.log_gen()
	trips_page_link = "https://mvrs.punjab.gov.pk/dev/axle/trip"
	enter_vehicle_load_data_link = "https://mvrs.punjab.gov.pk/dev/axle/trip/add"
	vehicle_reg_province_dropdown_id = "select2-reg_province-container"
	vehicle_reg_province_search_input_class = "select2-search__field"
	vehicle_reg_no_field_id = "vehicle_reg"
	vehicle_type_dropdown_id = "select2-no_of_axle-container"
	vehicle_type_search_input_class = "select2-search__field"
	unit_of_weight_dropdown_id = "select2-weight_unit-container"
	unit_of_weight_search_input_class = "select2-search__field"
	gross_weight_of_vehicle_field_name = "net_wight"
	origin_of_loading_goods_province_dropdown_id ="select2-org_province-container"
	origin_of_loading_goods_province_search_class = "select2-search__field"
	origin_of_loading_goods_district_dropdown_id = "select2-vehicle_origin-container"
	origin_of_loading_goods_district_search_class = "select2-search__field"
	destination_of_unloading_province_dropdown_id = "select2-destination_province-container"
	destination_of_unloading_province_search_class = "select2-search__field"
	destination_of_unloading_district_dropdown_id = "select2-vehicle_destination-container"
	destination_of_unloading_dsitrict_search_class = "select2-search__field"
	vehicle_driver_name_field_id = "driver_name"
	vehicle_driver_mobile_no_field_id = "driver_mobile"
	vehicle_driver_cnic_field_id = "driver_cnic"
	commodity_being_transported_dropdown_id = "select2-commodity-container"
	commodity_being_transported_search_class = "select2-search__field"
	sub_commodity_being_transported_dropdown_id = "select2-commodity_sub_menu-container"
	sub_commodity_being_transported_search_class = "select2-search__field"
	vehicle_picture_file_attachment_name = "image_front"
	reciept_picture_file_attachment_name = "image_receipt"
	save_trip_data_btn_class = "btn-danger"
	
	
	def __init__(self, driver):
		self.driver = driver
	
		
	def navigate_to_add_trip_form(self):
		self.driver.get(self.enter_vehicle_load_data_link)
		time.sleep(2)
		
	def enter_vehicle_registration_province(self):
		time.sleep(2)
		self.driver.find_element(By.ID, self.vehicle_reg_province_dropdown_id).click()
		self.driver.find_element(By.CLASS_NAME, self.vehicle_reg_province_search_input_class).send_keys("Pun")
		self.driver.find_element(By.CLASS_NAME,self.vehicle_reg_province_search_input_class).send_keys(Keys.ENTER)
	
	def enter_reg_no(self, Reg_No):
		vehicle_reg_no =  Reg_No
		self.driver.find_element(By.ID, self.vehicle_reg_no_field_id).send_keys(vehicle_reg_no)
		self.logger.info(f"---> Vehicle Reg No is: {vehicle_reg_no}")
	
	def select_vehicle_type(self):
		self.driver.find_element(By.ID, self.vehicle_type_dropdown_id).click()
		self.driver.find_element(By.CLASS_NAME, self.vehicle_type_search_input_class).send_keys("bedf")
		self.driver.find_element(By.CLASS_NAME,self.vehicle_type_search_input_class).send_keys(Keys.ENTER)

	def select_unit_of_weight(self):
		self.driver.find_element(By.ID, self.unit_of_weight_dropdown_id).click()
		self.driver.find_element(By.CLASS_NAME, self.unit_of_weight_search_input_class).send_keys("ton")
		self.driver.find_element(By.CLASS_NAME,self.unit_of_weight_search_input_class).send_keys(Keys.ENTER)
		###
	def enter_weight_value(self, weight):
		self.driver.find_element(By.NAME, self.gross_weight_of_vehicle_field_name).send_keys(weight)
		
	def select_origin_province(self):
		self.driver.find_element(By.ID, self.origin_of_loading_goods_province_dropdown_id).click()
		self.driver.find_element(By.CLASS_NAME, self.origin_of_loading_goods_province_search_class).send_keys("Punj")
		self.driver.find_element(By.CLASS_NAME,self.origin_of_loading_goods_province_search_class).send_keys(Keys.ENTER)
		
	def select_origin_district(self):
		time.sleep(3)
		self.driver.find_element(By.ID, self.origin_of_loading_goods_district_dropdown_id).click()
		self.driver.find_element(By.CLASS_NAME, self.origin_of_loading_goods_district_search_class).send_keys(Keys.DOWN + Keys.ENTER)
		
	def select_destination_province(self):
		self.driver.find_element(By.ID, self.destination_of_unloading_province_dropdown_id).click()
		self.driver.find_element(By.CLASS_NAME, self.destination_of_unloading_province_search_class).send_keys("Punj")
		self.driver.find_element(By.CLASS_NAME,self.destination_of_unloading_province_search_class).send_keys(Keys.ENTER)
	
	def select_destination_district(self):
		time.sleep(4)
		self.driver.find_element(By.ID, self.destination_of_unloading_district_dropdown_id).click()
		self.driver.find_element(By.CLASS_NAME, self.destination_of_unloading_dsitrict_search_class).send_keys(Keys.DOWN + Keys.ENTER)
	
	def enter_driver_name(self, driver_name):
		name = driver_name
		self.driver.find_element(By.ID, self.vehicle_driver_name_field_id).send_keys(name)
		self.logger.info(f"---> DRIVER NAME is: {name}")
	
	def enter_driver_mobile_no(self, mobile_no):
		phone = mobile_no
		self.driver.find_element(By.ID, self.vehicle_driver_mobile_no_field_id).send_keys(phone)
	
	def enter_driver_cnic(self, cnic):
		driver_cnic = cnic
		self.driver.find_element(By.ID, self.vehicle_driver_cnic_field_id).send_keys(driver_cnic)
		self.logger.info(f"---> Vehicle Driver CNIC is: {driver_cnic}")
		
	def select_commodity(self):
		self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)
		self.driver.find_element(By.ID, self.commodity_being_transported_dropdown_id).click()
		self.driver.find_element(By.CLASS_NAME, self.commodity_being_transported_search_class).send_keys("Food")
		self.driver.find_element(By.CLASS_NAME,self.commodity_being_transported_search_class).send_keys(Keys.ENTER)
		
	def select_sub_commodity(self):
		self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)
		self.driver.find_element(By.ID, self.sub_commodity_being_transported_dropdown_id).click()
		time.sleep(2)
		self.driver.find_element(By.CLASS_NAME, self.sub_commodity_being_transported_search_class).send_keys(Keys.DOWN + Keys.ENTER)

	def  upload_vehicle_front_picture(self, path):
		self.driver.find_element(By.NAME, self.vehicle_picture_file_attachment_name).send_keys(path)
		
	def  upload_reciept_picture(self, path):
		self.driver.find_element(By.NAME, self.reciept_picture_file_attachment_name).send_keys(path)
		
	def click_save_trip_data(self):
		time.sleep(1.5)
		self.driver.find_element(By.CLASS_NAME, self.save_trip_data_btn_class).click()