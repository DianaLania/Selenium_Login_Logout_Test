from selenium.webdriver.common.by import By
from SampleTest.Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = "password"
        self.login_button_XPATH = "//button[@type='submit']"

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, Locators.password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_XPATH).click()