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
        self.driver.get("https://www.amazon.in/")

    def test_search(self, setup):
        Search = self.driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
        Search.send_keys('iphone 16')
        Search_button = self.driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]')
        Search_button.click()
        print('search')

    def test_header(self, setup):
        Search = self.driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
        Search.send_keys('iphone 16')
        Search_button = self.driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]')
        Search_button.click()

        designs = self.driver.find_elements(By.XPATH, '//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]')
        print(designs)

        for i in designs:
            print(i.text)
        #
        # header1 = self.driver.find_element(By.XPATH, "//span[text()='iPhone 16 128 GB: 5G Mobile Phone with Camera Control, A18 Chip and a Big Boost in Battery Life. Works with AirPods; Black']")
        # print(header1.text)
        # header2 = self.driver.find_element(By.XPATH, "//span[text()='iPhone Air 1 TB: Thinnest iPhone Ever, 16.63 cm (6.5″) Display with Promotion up to 120Hz, Powerful A19 Pro Chip, Center Stage Front Camera, All-Day Battery Life; Sky Blue']")
        # print(header2.text)
        # header3 = self.driver.find_element(By.XPATH, "//span[text()='iPhone 16 256 GB: 5G Mobile Phone with Camera Control, A18 Chip and a Big Boost in Battery Life. Works with AirPods; Black']")
        # print(header3.text)
        # header4 = self.driver.find_element(By.XPATH, "//span[text()='iPhone 16 256 GB: 5G Mobile Phone with Camera Control, A18 Chip and a Big Boost in Battery Life. Works with AirPods; Black']")
        # print(header3.text)
        # print('success')



