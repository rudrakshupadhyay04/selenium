from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/broken_images')
driver.maximize_window()

images = driver.find_elements(By.TAG_NAME , 'img')

print(f"total number of images is: {len(images)}")

for img in images:
    src = img.get_attribute('src')
    response = requests.get(src)

    if response.status_code != 200:
        print(f"Broken images is: {src} (with status code: {response.status_code})")


driver.quit()