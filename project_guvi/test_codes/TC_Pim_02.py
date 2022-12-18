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

    def test_edit_pim_hrm(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)

        username = 'Admin'
        password = 'admin123'

        input_box_username = self.driver.find_element(by = By.NAME, value = 'username')
        input_box_password = self.driver.find_element(by = By.NAME, value = 'password')
        login_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

        input_box_username.send_keys(username)
        input_box_password.send_keys(password)
        login_xpath.click()
        time.sleep(7)

        pim_module_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        pim_module_xpath.click()
        time.sleep(9)

        employee_name = 'JAYAPRAKASH S'
        input_employee_name = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys(employee_name)
        search_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        time.sleep(5)
        id_xpath = self.driver.find_element(by= By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div').click()
        time.sleep(3)

        job_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a').click()
        time.sleep(3)
        job_title_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]').click()
        time.sleep(3)
        job_select_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]').click()
        time.sleep(5)
        save_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button').click()
        time.sleep(7)
        print("The user edited employee details successfully")




        