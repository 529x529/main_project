from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):

    url = 'https://www.saucedemo.com'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    user_name = "//input[@id = 'user-name']"
    password = "//input[@id = 'password']"
    login_button = "//input[@id = 'login-button']"

    #Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    #Actions

    def inpunt_username(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def inpunt_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods

    def autorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.inpunt_username("standard_user")
        self.inpunt_password("secret_sauce")
        self.click_login_button()



