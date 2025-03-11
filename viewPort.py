from selenium import webdriver
import time

viewPorts = [(1024,768), (768,1024) , (375,667)]

driver = webdriver.Chrome()
driver.get('https://google.com')

try:
    for width, height in viewPorts:
        driver.set_window_size(width,height)
        time.sleep(5)
finally:
    driver.close()
