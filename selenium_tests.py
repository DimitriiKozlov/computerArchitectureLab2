import unittest
from selenium import webdriver
import os
import time


class PalindromeTest(unittest.TestCase):

    def setUp(self):
        os.environ["SELENIUM_SERVER_JAR"] = "/Users/dimaster/PycharmProjects/selenium-server-standalone-2.45.0.jar"
        self.driver = webdriver.Safari()

    def test_index(self):
        driver = self.driver
        driver.get("http://localhost:8080")
        self.assertIn("Lab2::Worker", driver.title)
        # elem = driver.find_element_by_name("q")
        time.sleep(5)
        body = driver.find_element_by_tag_name("body")
        checktext = body.text
        assert "Last found palindromes:" in checktext

    def test_server(self):
        driver = self.driver
        driver.get("http://localhost:8080/server")
        driver.find_element_by_id("Restart").click()
        time.sleep(1)
        element = driver.find_element_by_id("percents")
        # element = driver.find_element_by_tag_name("body")
        checktext = 'Element check text: ' + element.text
        print(checktext)
        assert "Percents: 0" in checktext

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()