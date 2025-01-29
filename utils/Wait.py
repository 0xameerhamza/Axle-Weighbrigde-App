from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def wait_for_visibility(driver, ):
	wait = WebDriverWait(driver, 10)
	wait.until(EC.visibility_of_element_located((By.ID, "some_id")))


