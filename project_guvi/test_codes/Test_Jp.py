from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time


class Test_Jay:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()

    def get_title(self,booting_function):
        self.driver.get(self.url)
        assert self.driver.title == 'OrangeHRM'

    def test_login(self,booting_function):
        self.driver.get(self.url)
        time.sleep(7)
        self.driver.find_element(by = By.NAME, value = data.jay_selectors.input_box_name).send_keys(data.jay_data.username)
        self.driver.find_element(by = By.NAME, value = data.jay_selectors.input_box_password).send_keys(data.jay_data.password)
        self.driver.find_element(by = By.XPATH, value = data.jay_selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        print("The user is logged in successfully")

