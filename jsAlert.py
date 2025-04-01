from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://the-internet.herokuapp.com/javascript_alerts"

driver.get(url)

alertButton = driver.find_element(By.XPATH , "//button[normalize-space()='Click for JS Prompt']")
alertButton.click()

alert = driver.switch_to.alert
alertText = alert.text
print(alertText)


alert.send_keys("Hello i am learning selenium")
time.sleep(10)
alert.accept()
# alert.dismiss()


time.sleep(5)
driver.quit()