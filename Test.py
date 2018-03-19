import unittest

from selenium import webdriver
from login_page import LogInPage
# from login_page_my_class import LogInPage


class TestPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='resource/chromedriver.exe')

    def tearDown(self):
        self.driver.quit()

    def test_sign_in(self):
        page = LogInPage(self.driver)
        page.get('http://localhost:3000')
        page.login = 'dmytro'
        page.password = '1234'
        page.submit.click()


if __name__ == '__main__':
    unittest.main()
