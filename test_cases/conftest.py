import pytest
from selenium import webdriver
from utils.read_config import Read_Config

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    #driver.maximize_window()
    print("************************* START OF CONFTEST *************************")
    login_page_URL = Read_Config.get_login_page_url()
    driver.get(login_page_URL)
    return driver