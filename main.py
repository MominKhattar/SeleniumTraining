import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the .crx file for the Buster extension
crx_path = r"C:\Users\PMYL\OneDrive\Desktop\Python Practice\SeleniumTraining\Buster.crx"

selectorhub_path = r"C:\Users\PMYL\OneDrive\Desktop\Python Practice\SeleniumTraining\SelectorsHub.crx"


# Set up Chrome options
chrome_options = Options()
chrome_options.add_extension(crx_path)  # Add the extension
chrome_options.add_extension(selectorhub_path)  # Add the extension


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

# Switch to CAPTCHA iframe and click the checkbox
iframe = driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']")
driver.switch_to.frame(iframe)
driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border').click()

# Wait for the CAPTCHA modal to open
time.sleep(5)

# Switch to the CAPTCHA modal (assuming it's another iframe)
# You may need to inspect the modal structure to adjust this selector if it's different
try:
    # Switch to the modal iframe if it's a separate iframe
    modal_iframe = driver.find_element(By.XPATH, "//body/div/div[4]")

    driver.switch_to.frame(modal_iframe)

    # Click the Buster button (adjust the selector if needed)
    buster_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='g-recaptcha-bubble-arrow'])[2]"))
    )

    buster_button.click()  # Click the Buster button to solve the CAPTCHA

    # Wait for Buster to finish solving the CAPTCHA
    time.sleep(15)  # Adjust this time based on Buster's performance

except Exception as e:
    print(f"Buster button not found or CAPTCHA auto-solved. Error: {str(e)}")

# After CAPTCHA is solved, return to the main content frame
driver.switch_to.default_content()

# Finally, click the login button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Login'])[1]"))
)
login_button.click()

# Wait for a while to ensure the login process completes
time.sleep(5)

# Keep the browser open for manual debugging
input("Press Enter to close the browser...")

# Optional: Close the browser after debugging
driver.quit()
