from selenium import webdriver
import os

from selenium.webdriver.common.by import By

# os.environ['PATH'] += r"C:\Program Files (x86)\edgedriver_win64\msedgedriver.exe"

driver = webdriver.Firefox()

username = "standard_user"
userpassword  = "secret_sauce"
url = "https://www.saucedemo.com/"

driver.get(url)

username_field = driver.find_element(By.ID, value='user-name')
password_field = driver.find_element(By.ID, value='password')

login_button = driver.find_element(By.ID, value='login-button')

assert not login_button.get_attribute("disabled")

username_field.send_keys(username)
password_field.send_keys(userpassword)

login_button.click()


success_element = driver.find_element(By.CSS_SELECTOR, value='.title')
assert success_element.text == 'Products'