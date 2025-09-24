import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# IMPORTANT: Replace these with your actual username and password
username = "your_email@example.com"
password = "your_password"

# Set up the WebDriver using the correct Service object
# You need to specify the path to your chromedriver.exe
service = Service("C:\\Windows\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the Facebook login page
    driver.get("https://www.github.com/")

    # Find the username and password text boxes by their ID
    username_textbox = driver.find_element(By.ID, "email")
    password_textbox = driver.find_element(By.ID, "pass")

    # Enter the username and password
    username_textbox.send_keys(username)
    password_textbox.send_keys(password)

    # Find the login button by its name attribute and click it
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    # Wait for a few seconds to let the page load
    time.sleep(5)

    print("Login successful!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser window
    driver.quit()
