from pages.login_page import LoginPage
from config import BASE_URL, USERNAME, PASSWORD

def test_login(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login()

    assert login_page.verify_dashboard() == "Dashboard", \
        "Login failed - Dashboard not visible"


#this code work for POM but not fixture

# from selenium import webdriver
# from pages.login_page import LoginPage

# def test_login():
#     driver = webdriver.Chrome()
#     driver.get("https://opensource-demo.orangehrmlive.com/")
#     driver.maximize_window()

#     login_page = LoginPage(driver)

#     login_page.enter_username("Admin")
#     login_page.enter_password("admin123")
#     login_page.click_login()

#     assert login_page.verify_dashboard() == "Dashboard"

#     driver.quit()

