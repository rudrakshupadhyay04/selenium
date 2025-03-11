from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

loginUrl = 'https://www.saucedemo.com/'
username = 'standard_user'
password = 'secret_sauce'

driver.get(loginUrl)

inputField = driver.find_element(By.ID, 'user-name')
passwordField = driver.find_element(By.ID, 'password')

inputField.send_keys(username)
passwordField.send_keys(password)

loginButton = driver.find_element(By.ID, "login-button")
assert not loginButton.get_attribute('disabled')
loginButton.click()

successElement = driver.find_element(By.CSS_SELECTOR, ".title")
assert successElement.text == 'Products'


time.sleep(10)

driver.quit()