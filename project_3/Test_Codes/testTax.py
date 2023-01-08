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

        #tax_exemptions
        tax_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a').click()
        time.sleep(3)
        federal = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]')
        action = ActionChains(self.driver)
        action.click(on_element = federal)
        action.perform()
        time.sleep(3)
        single_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]').click()
        time.sleep(3)
        self.exemp = "1"
        exe_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input').send_keys(self.exemp)
        time.sleep(3)
        state_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]')
        action_2 = ActionChains(self.driver)
        action_2.click(on_element = state_xpath)
        action_2.perform()
        time.sleep(2)
        indiana_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div[25]').click()
        time.sleep(3)
        status_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div')
        action_3 = ActionChains(self.driver)
        action_3.click(on_element = status_xpath)
        action_3.perform()
        single_2 = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]').click()
        time.sleep(3)
        self.exemptions = "3"
        exo_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input').send_keys(self.exemptions)
        time.sleep(2)
        unemploy = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div')
        action_4 = ActionChains(self.driver)
        action_4.click(on_element = unemploy)
        action_4.perform()
        time.sleep(4)
        pennysl_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div[2]/div[52]').click()
        time.sleep(5)
        work_state = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[1]')
        action_5 = ActionChains(self.driver)
        action_5.click(on_element = work_state)
        action_5.perform()
        time.sleep(3)
        new_york = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div[2]/div[44]').click()
        time.sleep(5)
        save_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button').click()
        time.sleep(3)
        print("Thse user should be able to see the Tax Exemptions details in their own page successfully")