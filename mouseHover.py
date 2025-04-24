from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
driver.get(url)
time.sleep(5)

# to automate low level interactions such as mouse movements, mouse button actions, key press ActionChains is used
actions = ActionChains(driver)

hoverElement = driver.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
actions.move_to_element(hoverElement).perform()
time.sleep(5)

driver.find_element(By.XPATH, "//a[normalize-space()='Frames']").click()


time.sleep(5)

driver.quit()

