# Borwser methods and property

from selenium import webdriver

driver = webdriver.Chrome()

driver.get()
driver.find_element()
driver.maximize_window()
driver.minimize_window()
driver.fullscreen_window()
driver.back()
driver.forward()
driver.refresh()
driver.close()

driver.title  #-- this is a property