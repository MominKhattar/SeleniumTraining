from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Correct path for your Chrome profile
chrome_profile_path = r"C:\Users\PMYL\AppData\Local\Google\Chrome\User Data"

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")  # Set profile path to Chrome user data folder
chrome_options.add_argument("--profile-directory=Default")  # Use the Default profile (or Profile 1, Profile 2, etc.)
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--remote-debugging-port=9222")  # Optional: Enable remote debugging

# Initialize WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

# URL and login credentials
url = "https://blsitalypakistan.com/account/login"
username = "guestuse3309@gmail.com"
password = "khan98765"

# Open the website
driver.get(url)

# Find and fill in the username and password fields
user_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
user_field.send_keys(username)

password_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']")
password_field.send_keys(password)

# Find the login button and click it
login_button = driver.find_element(By.NAME, "submitLogin")
login_button.click()
