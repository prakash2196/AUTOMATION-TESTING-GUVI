from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

class Test_Jay:
     url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
     @pytest.fixture
     def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()

     def test_employ_tax(self,booting_function):

        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)

        self.username = 'Admin'
        self.password = 'admin123'

        input_box_username = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(self.username)
        input_box_password = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(self.password)
        login_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(5)

        pim_create = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        time.sleep(3)
        employ_list = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a').click()
        time.sleep(3)
        self.name = 'Jaya Prakash'
        employ_name = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys(self.name)
        search_employ = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        time.sleep(3)
        search_open = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div').click()
        time.sleep(3)

        #employee_job_details
        job_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a').click()
        time.sleep(2)
        job_title = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]')
        action = ActionChains(self.driver)
        action.click(on_element = job_title)
        action.perform()
        xpath_1 = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]').click()
        time.sleep(3)
        job_category = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]')
        action_1 = ActionChains(self.driver)
        action_1.click(on_element = job_category)
        action_1.perform()
        time.sleep(3)
        professional_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[7]').click()
        time.sleep(3)
        sub_unit = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[1]')
        action_3 = ActionChains(self.driver)
        action_3.click(on_element = sub_unit)
        action_3.perform()
        time.sleep(3)
        engineering_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div[2]/div[3]').click()
        time.sleep(3)
        location_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]')
        action_4 = ActionChains(self.driver)
        action_4.click(on_element = location_xpath)
        action_4.perform()
        time.sleep(3)
        new_york = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[4]').click()
        time.sleep(5)
        employment_status = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div')
        action_5 = ActionChains(self.driver)
        action_5.click(on_element = employment_status)
        action_5.perform()
        time.sleep(3)
        part_time_internship = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div[2]/div[7]').click()
        time.sleep(5)
        include = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span').click()
        time.sleep(3)
        self.start_date = "2021-09-07"
        start_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input').send_keys(self.start_date)
        time.sleep(3)
        self.end_date = "2022-10-15"
        end_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input').send_keys(self.end_date)
        time.sleep(3)
        save_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button').click()
        time.sleep(3)
        print("The user should be able to see all the filled details present in Job Details page successfully ")