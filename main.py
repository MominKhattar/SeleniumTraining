from selenium import webdriver
from selenium.webdriver.common.by import By

driver =  webdriver.Chrome()

url = "https://blsitalypakistan.com/account/login"

username = "guestuse3309@gmail.com"
password = "khan98765"
driver.get(url)

user_field = driver.findElement(By.xpath("//input[@placeholder='Enter Email']"))
password_field = driver.findElement(By.xpath("//input[@placeholder='Enter Password']"))

captcha = driver.findElement(By.className("vsc-initialized"))

login_button = driver.findElement(By.name("submitLogin"))
login_button

