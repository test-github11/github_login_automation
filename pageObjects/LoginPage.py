from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    sign_in_button = (By.XPATH, "//a[@href='/login']")

    def sign_in_button_m(self):
        return self.driver.find_element(*LoginPage.sign_in_button)

    username = (By.XPATH, "//input[@name='login']")

    def user_name_m(self):
        return self.driver.find_element(*LoginPage.username)

    password = (By.NAME, "password")

    def pass_word_m(self):
        return self.driver.find_element(*LoginPage.password)

    submit = (By.CSS_SELECTOR, "input[name='commit']")

    def submit_m(self):
        return self.driver.find_element(*LoginPage.submit)