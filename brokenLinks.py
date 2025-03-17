from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

url = 'https://jqueryui.com/'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

allLinks = driver.find_elements(By.TAG_NAME, 'a');

print(f'Total number of links is "{len(allLinks)}"')

for link in allLinks:
    href = link.get_attribute('href')
    response = requests.get(href, timeout=20)
    
    if response.status_code >= 400:
        print(f"Broken Link is: {href} (Status Code is: {response.status_code})")




driver.quit()
