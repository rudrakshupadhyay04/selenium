from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from selenium.webdriver import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.globalsqa.com/demo-site/datepicker/"

driver.get(url)
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click()

frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")

driver.switch_to.frame(frame)
time.sleep(5)
datepicker = driver.find_element(By.XPATH, "//input[@id='datepicker']")

datepicker.click()

# time.sleep(5)

currentDate = datetime.now()

nextDate = currentDate + timedelta(days=2)
# print(nextDate)

previousDate = currentDate + timedelta(days= -1)
# print(previousDate)

formattedDate = previousDate.strftime('%m/%d/%y')

datepicker.send_keys(formattedDate + Keys.ENTER)

time.sleep(5)


driver.quit()
