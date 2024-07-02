from selenium import webdriver
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        # options.binary_location = '../drivers/chromedriver.exe'
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.refresh()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")
        self.driver.find_element("name", "q").send_keys("Automation Step by Step")
        self.driver.find_element("name", "btnK").click()

    def test_search_pandu(self):
        self.driver.get("https://google.com")
        self.driver.find_element("name", "q").send_keys("Batman Costumes")
        self.driver.find_element("name", "btnK").click()
        self.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='D:\\Data Engineering Project\\ML Project\\Selenium Essentials\\Application Search\\reports'))
