import unittest
from selenium import webdriver


class IntegralTest(unittest.TestCase):
    def test_server(self):
        print "TESTING SERVER"
        driver = webdriver.Firefox()
        driver.get("http://0.0.0.0:8084/server")

        self.assertIn("Lab2::Server", driver.title)
        body = driver.find_element_by_tag_name("body")

        check_text = body.text
        assert "Last count integral:" in check_text

    def test_worker(self):
        print "TESTING WORKER"
        driver = webdriver.Firefox()
        driver.get("http://0.0.0.0:8084")

        self.assertIn("Lab2::Worker", driver.title)

        driver.find_element_by_id("Restart").click()
        element = driver.find_element_by_id("percents")
        check_text = element.text
        print('Element check text: ' + check_text)
        assert "Percents:" in check_text


if __name__ == "__main__":
    unittest.main()