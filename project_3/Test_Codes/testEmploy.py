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

     def test_employ_personal(self,booting_function):

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

        #employee_personal_details
        self.nickname = "cheeku"
        nick_name = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input').send_keys(self.nickname)
        time.sleep(2)
        self.other_lic = "BAEPJ0765L"
        lic_num = self.driver.find_element(by = By.XPATH, value ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys(self.other_lic)
        time.sleep(2)
        gender_male = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label').click()
        time.sleep(3)
        nationality_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]')
        action = ActionChains(self.driver)
        action.click(on_element = nationality_xpath)
        action.perform()
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[27]').click()
        time.sleep(3)
        martial_status = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div')
        action_1 = ActionChains(self.driver)
        action_1.click(on_element = martial_status)
        action_1.perform()
        time.sleep(2)
        single_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]').click()
        time.sleep(3)
        save_xpath = self.driver.find_element(by = By.XPATH, value ='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button').click()
        print("The user should be able to see all the filled details present in Personal Details page successfully")