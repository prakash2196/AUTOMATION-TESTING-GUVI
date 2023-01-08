from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

class Test_Search:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()

    def test_search_box(self,booting_function):
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.get(self.url)
        time.sleep(3)

        self.username = "Admin"
        self.password = "admin123"
        

        useraname_xpath = self.driver.find_element(by = By.XPATH, value =  '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(self.username)
        password_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(self.password)
        login_button = self.driver.find_element(by = By.XPATH, value =  '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(3)

        

        search_box = self.driver.find_element(by = By.XPATH , value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        time.sleep(3)
        self.search_param = "Buzz"
        search_box.send_keys(self.search_param)
        time.sleep(2)

        print("The user should be able to search the mentioned Admin Page Menu and these inidividual menu name should be displayed under search text box")
        

