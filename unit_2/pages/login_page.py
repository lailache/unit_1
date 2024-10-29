from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def is_error_message_displayed(self):
        error_message = self.driver.find_element(By.CSS_SELECTOR, "Epic sadface: Username is required")
        return error_message.is_displayed()


