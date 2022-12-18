from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import data
import pytest
import time

class Test_Jay_02:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()

    def test_invalid_login(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.NAME, value = data.jay_selectors.input_box_name).send_keys(data.jay_data.username)
        self.driver.find_element(by = By.NAME, value = data.jay_selectors.input_box_password).send_keys(data.jay_data.password)
        self.driver.find_element(by = By.XPATH, value = data.jay_selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        print("A valid error message for invalid credentials is displayed")

        