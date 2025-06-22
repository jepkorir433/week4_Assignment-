# test_login.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Function to test login
def test_login(username, password, test_name):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)  # wait for page to load

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)

    if "Logged In Successfully" in driver.page_source:
        print(f"{test_name}: SUCCESS ✅")
    elif "Your username is invalid!" in driver.page_source or "Your password is invalid!" in driver.page_source:
        print(f"{test_name}: INVALID LOGIN ❌")
    else:
        print(f"{test_name}: UNKNOWN RESULT ⚠️")

# Test 1: Valid Login
test_login("student", "Password123", "Test Valid Login")

# Test 2: Invalid Login
test_login("wronguser", "wrongpassword", "Test Invalid Login")

# Close browser after tests
time.sleep(2)
driver.quit()
input("Press Enter to close browser...")
# Test 1: Valid Login
# test_login("student", "Password123", "Test Valid Login")

# Test 2: Invalid Login
test_login("wronguser", "wrongpassword", "Test Invalid Login")


