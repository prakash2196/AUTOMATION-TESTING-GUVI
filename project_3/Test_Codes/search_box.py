 #def search_PIM(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)
        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        pim_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()

    #def search_Leave(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        leave_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a').click()

    #def search_Time(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        time_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a').click()

    #def search_Recruitment(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        recruitment_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a').click()

    #def search_My_Info(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        info_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()

    #def search_Performance(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        performance_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span').click()

    #def search_Dashboard(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        dashboard_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()

    #def search_Directory(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        directory_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a').click()

    #def search_Maintenance(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        maintenance_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span').click()

    #def search_Buzz(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        buzz_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a').click()

s.search_PIM("PIM")

#s.search_Leave("Leave")

#s.search_Time("Time")

#s.search_Recruitment("Recruitment")

#s.search_My_Info("My_Info")

#s.search_performance("Performance")

#s.search_Dashboard("Dashboard")

#s.search_Directory("Directory")

#s.search_Maintenance("Maintenance")

#s.search_Buzz("Buzz")