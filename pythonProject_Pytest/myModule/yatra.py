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
        self.driver.get("https://www.yatra.com/")

    def test_search(self, setup):
        close_btn = self.driver.find_element(By.XPATH, '//span[@class="style_cross__q1ZoV"]/img[@alt="cross"]')
        close_btn.click()
        departure_city = self.driver.find_element(By.XPATH, "(//div[@class='MuiBox-root css-1ek1ggs'])[1]")
        departure_city.click()
        dropdown_selection = self.driver.find_element(By.XPATH, "//div[text()='Mumbai, (BOM)']")
        dropdown_selection.click()
        going_to = self.driver.find_element(By.XPATH, "(//div[@class='MuiBox-root css-1ek1ggs'])[2]")
        going_to.click()
        dropdown_selection = self.driver.find_element(By.XPATH, "//div[text()='Bangalore, (BLR)']")
        dropdown_selection.click()
        click_Search = self.driver.find_element(By.XPATH, '(//button[@type="button"])[2]')
        click_Search.click()
        print('search')

    # def test_header(self, setup):
    #     Search = self.driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
    #     Search.send_keys('iphone 16')
    #     Search_button = self.driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]')
    #     Search_button.click()