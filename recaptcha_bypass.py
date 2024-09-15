from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# from main import buster_button

# GOOGLE RECAPTCHA BYYPASSER

# Path to the .crx file for the Buster extension
crx_path = r"C:\Users\Haider Computer\Desktop\SeleniumTraining\Buster.crx"
selectorhub_path = r'C:\Users\Haider Computer\Desktop\SeleniumTraining\SelectorsHub.crx'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_extension(crx_path)  # Add the Buster extension
chrome_options.add_extension(selectorhub_path)  # Add the SelectorsHub extension

# Optional: Prevent Chrome from closing at the end (for debugging)
chrome_options.add_experimental_option("detach", True)

# Initialize WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the page with reCAPTCHA
driver.get("https://google.com/recaptcha/api2/demo")

# Click the reCAPTCHA checkbox
iframe = driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']")
driver.switch_to.frame(iframe)
driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border').click()

# Switch back to the main content and wait for the challenge iframe
driver.switch_to.default_content()

# Wait and print all iframes (debugging to make sure you find the right one)
iframes = driver.find_elements(By.TAG_NAME, 'iframe')
for idx, iframe in enumerate(iframes):
    print(f"Iframe {idx}: {iframe.get_attribute('src')}")

# Find the challenge iframe and switch to it
challenge_iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//iframe[@title="recaptcha challenge expires in two minutes"]'))
)
driver.switch_to.frame(challenge_iframe)

# Pause to ensure the page is fully loaded
# time.sleep(2)

# Try finding the Buster button again
try:
    buster_button = WebDriverWait(driver,5).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="rc-imageselect"]/div[3]/div[2]/div[1]/div[1]/div[4]')
        )
    )
    buster_button.click()

#    buster_button = driver.find_element(By.XPATH, '//*[@id="rc-imageselect"]/div[3]/div[2]/div[1]/div[1]/div[4]')
#    buster_button.click()
except Exception as e:
    print(f"Error finding Buster button: {e}")
    driver.quit()

# Wait for Buster to solve the CAPTCHA (this might take a while)
# time.sleep(10)  # Adjust the sleep time if needed

# Switch back to the reCAPTCHA iframe to check if the CAPTCHA is solved
driver.switch_to.default_content()
recaptcha_iframe = driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']")
driver.switch_to.frame(recaptcha_iframe)

# Check if the CAPTCHA is solved by checking the aria-checked attribute
checkbox = driver.find_element(By.ID, 'recaptcha-anchor')

# Polling loop to wait for CAPTCHA to be solved
captcha_solved = False
while not captcha_solved:
  #  time.sleep(1)
    captcha_solved = checkbox.get_attribute('aria-checked') == 'true'
    print("Waiting for CAPTCHA to be solved...")

# CAPTCHA solved, now submit the form
print("CAPTCHA solved. Submitting the form.")
driver.switch_to.default_content()
submit_button = driver.find_element(By.ID, 'recaptcha-demo-submit')
submit_button.click()

# Optional: Wait or close the browser
# driver.implicitly_wait(10)
# driver.quit()
