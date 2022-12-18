from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import data
import pytest
import time

class Test_Jay_03:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()

    def test_delete_pim(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(5)

        username = 'Admin'
        password = 'admin123'

        input_box_username = self.driver.find_element(by = By.NAME, value = 'username')
        input_box_password = self.driver.find_element(by = By.NAME, value = 'password')
        login_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

        input_box_username.send_keys(username)
        input_box_password.send_keys(password)
        login_xpath.click()
        time.sleep(7)
        assert self.driver.title == 'OrangeHRM'

        pim_module_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
        time.sleep(3)

        employee_name_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys('JAYAPRAKASH S')
        search_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        time.sleep(5)

        delete_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]/i').click()

        print("the user deleted an employee details what he created successfully")






