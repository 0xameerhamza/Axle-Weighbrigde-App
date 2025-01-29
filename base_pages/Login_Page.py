from selenium.webdriver.common.by import By
from utils.read_captcha import Read_Captcha


class LoginPage:
    username_field_Name = "username"
    password_field_Name = "password"
    sign_in_button_class = "btn-primary"
    captcha_Image_div_id = "captcha_img"
    captchaField_id = "captcha"
    Logout_button_xpath = "//span[text()='Logout']"


    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_field_Name).clear()
        self.driver.find_element(By.NAME, self.username_field_Name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_field_Name).clear()
        self.driver.find_element(By.NAME, self.password_field_Name).send_keys(password)

    def get_captcha_image(self):
        self.driver.find_element(By.ID, self.captcha_Image_div_id).screenshot(".\\temp\\CaptchaScreenshot.png")
        self.Screenshot_Path = ".\\temp\\CaptchaScreenshot.png"

    def enter_captcha_text(self):
        self.get_captcha_image()
        Captcha_text = Read_Captcha(self.Screenshot_Path)
        self.driver.find_element(By.ID, self.captchaField_id).send_keys(Captcha_text)

    def click_SignIn(self):
        self.driver.find_element(By.CLASS_NAME, self.sign_in_button_class).click()

    def click_Logout(self):
        self.driver.get("https://mvrs.punjab.gov.pk/dev/axle/logout")
    
    def close_driver(self):
        self.driver.close()
        print("Driver Closed")

