from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver.support.wait import WebDriverWait

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


# Navigate to the page
driver.get("https://google.com/recaptcha/api2/demo")
# driver.implicitly_wait(5)
chrome_options.add_experimental_option("detach", True)


# Click the reCAPTCHA checkbox
# Switch to CAPTCHA iframe and click the checkbox

iframe = driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']")
driver.switch_to.frame(iframe)
driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border').click()


#  driver.switch_to.default_content()
time.sleep(8)

driver.find_element(By.XPATH,"//div[@class='button-holder help-button-holder']").click()

# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "c-iy7y7qzhmp44")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='solver-button']"))).click()
