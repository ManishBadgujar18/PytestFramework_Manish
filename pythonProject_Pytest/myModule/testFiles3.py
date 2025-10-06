import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSmoke:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def test_Login(self, setup):

        username= self.driver.find_element(By.XPATH, '//input[@name="username"]')
        username.send_keys('Admin')
        password= self.driver.find_element(By.XPATH, '//input[@name="password"]')
        password.send_keys('admin123')
        login_button= self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
        print('Login')

    def test_AdminPage(self, setup):
        username = self.driver.find_element(By.XPATH, '//input[@name="username"]')
        username.send_keys('Admin')
        password = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        password.send_keys('admin123')
        login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()

        select_admin=self.driver.find_element(By.XPATH, '//span[text()="Admin"]')
        select_admin.click()

        select_edit=self.driver.find_element(By.XPATH, "(//i[contains(@class, 'bi-pencil-fill')])[1]")
        select_edit.click()

        data_entry=self.driver.find_element(By.XPATH, '//input[@placeholder="Type for hints..."]')
        data_entry.send_keys()

        enter_data=self.driver.find_element(By.XPATH, '//input[@autocomplete="off"]')
        enter_data.send_keys()

        click_button =self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        click_button.click()
        time.sleep(5)
        print(' successfully added Admin entry data')


