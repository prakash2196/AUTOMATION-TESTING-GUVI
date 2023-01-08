from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

class Test_Admin:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()

    def test_login_admin(self,booting_function):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.username = 'Admin'
        self.password = 'admin123'

        self.input_box_username = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
        self.input_box_password = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        self.login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)
        admin_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
        time.sleep(3)
        admin_username = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys(self.username)
        time.sleep(2)
        user_role = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]')
        action = ActionChains(self.driver)
        action.click(on_element = user_role)
        action.perform()
        ess_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]').click()
        time.sleep(3)
        self.employee_name = "Jaya Prakash"
        employee_name_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input').send_keys(self.employee_name)
        time.sleep(2)
        status_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]')
        action_1 = ActionChains(self.driver)
        action_1.click(on_element = status_xpath)
        action_1.perform()
        disabled_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[3]').click()
        time.sleep(2)
        add_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(3)
        print("The user should able to see ESS-Disabled and Admin-Enabled successfully")