import time
import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

class TestAPIEndpoints(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')  # Run in headless mode
        service = Service("/usr/local/bin/geckodriver")
        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.get("http://localhost:3003")  # URL of your React app

    def tearDown(self):
        # Clean up after each test
        self.driver.quit()

    def test_error_500(self):
        """Test the 500 Error endpoint by directly hitting the API."""
        # Hit the API endpoint for 500 error
        response = requests.get("http://localhost:5000/api/error500")
        self.assertEqual(response.status_code, 500)  # Assert that it returns a 500 status code

        # Optionally, check the response content if needed
        self.assertIn("Internal Server Error", response.text)

    def test_error_404(self):
        """Test the 404 Error endpoint by directly hitting the API."""
        # Hit the API endpoint for 404 error
        response = requests.get("http://localhost:5000/api/error404")
        self.assertEqual(response.status_code, 404)  # Assert that it returns a 404 status code

        # Optionally, check the response content if needed
        self.assertIn("Not Found", response.text)

    def test_delay(self):
        """Test the delayed response endpoint by directly hitting the API."""
        # Hit the API endpoint for delayed response
        response = requests.get("http://localhost:5000/api/delay")
        
        # Wait for the delay (adjust to match expected delay time)
        self.assertEqual(response.status_code, 200)  # Assert the status code is 200 (OK)
        self.assertIn("Delayed response", response.text)

    def db_delay(self):
        response = request.get("")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Slow DB", response.text)

    def test_browser_load(self):
        """Test that the browser loads correctly."""
        page_title = self.driver.title
        self.assertEqual(page_title, "React + Flask Error Simulation")

if __name__ == "__main__":
    unittest.main()
