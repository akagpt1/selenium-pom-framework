from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")

    # Actions
    def enter_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def verify_dashboard(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.dashboard_header)
        ).text
