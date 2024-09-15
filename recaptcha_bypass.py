from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Path to the .crx file for the Buster extension
crx_path = r"C:\Users\Haider Computer\Desktop\SeleniumTraining\Buster.crx"

selectorhub_path = r'C:\Users\Haider Computer\Desktop\SeleniumTraining\SelectorsHub.crx'

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
driver.implicitly_wait(5)

driver.switch_to.default_content()
iframe = driver.find_element(By.XPATH, '//iframe[@title="recaptcha challenge expires in two minutes"]')
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, '//*[@id="rc-imageselect"]/div[3]/div[2]/div[1]/div[1]/div[4]').click()
driver.implicitly_wait(10)

driver.switch_to.default_content()
driver.find_element(By.ID, 'recaptcha-demo-submit').click()

# driver.switch_to.default_content()
# iframe = driver.find_element(By.XPATH, '')
