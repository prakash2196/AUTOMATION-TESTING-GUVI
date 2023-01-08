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

     def test_employ_salary(self,booting_function):

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

        #updating_employee_salary
        salary_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a').click()
        time.sleep(3)
        add_component = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button').click()
        time.sleep(5)
        self.salary_component = "Basic"
        compo_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys(self.salary_component)
        time.sleep(3)
        frequency_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div')
        action_1 = ActionChains(self.driver)
        action_1.click(on_element = frequency_xpath)
        action_1.perform()
        monthly_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[4]').click()
        time.sleep(3)
        currency_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div')
        action_2 = ActionChains(self.driver)
        action_2.click(on_element = currency_xpath)
        action_2.perform()
        time.sleep(4)
        indian_rupee_xpath = self.driver.find_element(by = By.XPATH,value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[63]').click()
        time.sleep(3)
        self.amount = "15000"
        amount_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input').send_keys(self.amount)
        time.sleep(2)
        include_direct_deposit = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label/span').click()
        time.sleep(3)
        self.account_num = "6538748859"
        account_number_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input').send_keys(self.account_num)
        time.sleep(3)
        account_type = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div/div[1]')
        action_3 = ActionChains(self.driver)
        action_3.click(on_element = account_type)
        action_3.perform()
        savings_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]').click()
        time.sleep(3)
        self.acc_amt = "12000"
        acc_xpath_amt = self.driver.find_element(by = By.XPATH, value  = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input').send_keys(self.acc_amt)
        time.sleep(3)
        self.routing_num = "041215032"
        roting_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input').send_keys(self.routing_num)
        time.sleep(3)
        save_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[2]').click()
        time.sleep(3)
        print("The user should be able to see Salary and Deposit on Salary Details page successfully")
