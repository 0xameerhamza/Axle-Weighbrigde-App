import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import table_handler


class ViewTrip:
	view_trips_page_link = "https://mvrs.punjab.gov.pk/dev/axle/trip"
	driver_name_search_field_name = "driver_name"
	reg_no_search_field_name = "reg_no"
	vehicle_stats_filter_id = "select2-vstatus-container"
	vehicle_stats_search_field_class = "select2-search__field"
	filter_search_btn_id = "btn-search"
	
	table_xpath = ".//table"
	driver_name_column_no = 4
	vehicle_reg_no_column_no = 5
	

	def __init__(self, driver):
		self.driver = driver
		
	def navigate_to_view_trip_page(self):
		self.driver.get(self.view_trips_page_link)
		
	def search_trip_by_reg_no(self, reg_no):
		time.sleep(1)
		self.driver.find_element(By.NAME, self.reg_no_search_field_name).send_keys(reg_no)
		self.driver.find_element(By.ID, self.vehicle_stats_filter_id).click()
		time.sleep(1)
		self.driver.find_element(By.CLASS_NAME, self.vehicle_stats_search_field_class).send_keys("ALL")
		self.driver.find_element(By.CLASS_NAME, self.vehicle_stats_search_field_class).send_keys(Keys.ENTER)
		self.driver.find_element(By.ID, self.filter_search_btn_id).click()
		time.sleep(2)
		
	def get_driver_name(self):
		self.driver.execute_script("window.scrollBy(0, 192);")
		time.sleep(2)
		name_cell = table_handler.get_cell_value(self.driver, 1, self.driver_name_column_no)
		return name_cell

	
	def get_vehicle_reg_no(self):
		time.sleep(1)
		reg_no_cell = table_handler.get_cell_value(self.driver, 1, self.vehicle_reg_no_column_no)
		return reg_no_cell