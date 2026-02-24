from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 30)

username = wait.until(
    EC.visibility_of_element_located((By.NAME, "username"))
)
username.send_keys("Admin")

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_btn.click()

try:
    dashboard=wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h6.oxd-text--h6"))
    )
    assert dashboard.text == "Dashboard"
    print("Login Successful")

except Exception as e:
    driver.save_screenshot("login_fail.png")
    print("Login Failed")
    print("error:",e)
    
finally:    
    driver.quit()
