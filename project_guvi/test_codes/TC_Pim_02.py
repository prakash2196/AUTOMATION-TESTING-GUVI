from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

class Test_Jay_03:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()

    def edit_pim_hrm(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        