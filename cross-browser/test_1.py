import os
from time import sleep
from selenium import webdriver


class TestBrowser:
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=os.path.dirname(__file__) + "\chromedriver", options=op)
    a = 2

    def test_demo1(self):
        print("test passed")

    def test_demo2(cls):
        driver = cls.driver
        driver.get("https://www.google.com/")
        sleep(3)
        driver.close()
