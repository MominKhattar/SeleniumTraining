from selenium import webdriver
import os

# os.environ['PATH'] += r"C:\Program Files (x86)\edgedriver_win64\msedgedriver.exe"

driver = webdriver.Firefox()

driver.get("https://www.selenium.dev/")

driver.maximize_window()

title = driver.title

print(title)

# assert "Seleniuewewm" in title

