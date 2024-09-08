import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Path to the .crx file
crx_path = r"C:\Users\PMYL\OneDrive\Desktop\Python Practice\SeleniumTraining\Buster.crx"
# Set up Chrome options
chrome_options = Options()
chrome_options.add_extension(crx_path)  # Add the extension


# Optional: Prevent Chrome from closing at the end (for debugging)
chrome_options.add_experimental_option("detach", True)

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


iframe = driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']")
driver.switch_to.frame(iframe)
driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border').click()

# Wait for a short period to see if CAPTCHA is solved automatically
time.sleep(5)  # Wait for CAPTCHA to attempt auto-solving


# Finally, click the login button
driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]").click()

# Wait for a while to ensure the login process completes
time.sleep(5)

# Keep the browser open for manual debugging
input("Press Enter to close the browser...")

# Optional: Close the browser after debugging
driver.quit()