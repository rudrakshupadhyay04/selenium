from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.execute_script("window.scrollTo(0,700)")

# -----------------
table = driver.find_element(By.ID, 'countries')
rows = table.find_elements(By.TAG_NAME, 'tr')
rowsCount = len(rows)
print(f"Number of rows is {rowsCount}")

# -----------------------------------
target = "Australia"
found = False

for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    for cell in cells:
        if target in cell.text:
            print(f'Found target value "{target}"')
            found = True
            break

    if found:
        break

if not found:
    print(f"Target value '{target}' not found")



time.sleep(5)
driver.quit()