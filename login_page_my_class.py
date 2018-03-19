class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LogInPage(BasePage):

    def enter_login(self, login):
        login_field = self.driver.find_element_by_name('login')
        login_field.sendkeys(login)

    def enter_password(self, password):
        password_field = self.driver.find_element_by_name('password')
        password_field.senkeys(password)

    def submit(self):
        self.driver.find_element_by_class('submit fa fa-check-circle-o fa-3x').click()

