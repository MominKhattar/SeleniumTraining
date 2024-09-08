import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your Chrome profile (remove the Default directory from here, will specify profile below)
chrome_profile_path = r"C:\Users\PMYL\AppData\Local\Google\Chrome\User Data"

# Configure Chrome options to include your profile with the Buster extension installed
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")
chrome_options.add_argument("--profile-directory=Default")  # Ensure the right profile is selected
chrome_options.add_argument("--start-maximized")

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

# Wait until CAPTCHA is visible and clickable
# captcha_checkbox = WebDriverWait(driver, 10).until(
 #   EC.element_to_be_clickable((By.XPATH, "//div[@class='recaptcha-checkbox-border']"))
#)


iframe = driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']")
# iframe = driver.find_element(By.ID, 'recaptcha-anchor')
driver.switch_to.frame(iframe)
driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border').click()


# Click on the CAPTCHA checkbox
#captcha_checkbox.click()

# Wait for a short period to see if CAPTCHA is solved automatically
time.sleep(5)  # Wait for CAPTCHA to attempt auto-solving

# Check if CAPTCHA challenge opens (images or audio)

'''
try:
    captcha_frame = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[@title='recaptcha challenge']"))
    )
    # Switch to CAPTCHA frame
    driver.switch_to.frame(captcha_frame)

    # Try finding the Buster button (Orange button at the bottom)
    buster_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "help-button-holder"))
    )
    buster_button.click()  # Click the Buster button to switch to audio CAPTCHA

    # Wait for audio CAPTCHA and play button to appear
    play_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "rc-audiochallenge-play-button"))
    )
    play_button.click()  # Click the play button for audio CAPTCHA

    # Wait for Buster to solve the CAPTCHA (this may take a few seconds)
    time.sleep(15)

    # After CAPTCHA is solved, return to the main content frame
    driver.switch_to.default_content()

except Exception as e:
    print("No additional CAPTCHA challenge detected. Proceeding...")

    '''

# Finally, click the login button
driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]").click()

# Wait for a while to ensure the login process completes
time.sleep(5)

# Keep the browser open for manual debugging
input("Press Enter to close the browser...")

# Optional: Close the browser after debugging
driver.quit()