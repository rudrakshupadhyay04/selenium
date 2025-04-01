from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

iframe = driver.find_element(By.ID , 'mce_0_ifr')
driver.switch_to.frame(iframe) #switching to iframe window

textEditor = driver.find_element(By.ID, 'tinymce')
# textEditor.clear() # this also not work due to paid version
# textEditor.send_keys("Learning iframe handling") # it doses not work due to paid version


# outside the iframe
driver.switch_to.default_content()
link = driver.find_element(By.XPATH, "//a[normalize-space()='Elemental Selenium']")
link.click()

time.sleep(5)
driver.quit()