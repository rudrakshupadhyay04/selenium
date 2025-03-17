from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.maximize_window()

loginUrl = 'https://the-internet.herokuapp.com/dropdown'
driver.get(loginUrl)

dropdown = driver.find_element(By.ID,'dropdown')
select = Select(dropdown)

# ----------------------------
# checking the count 
expectedCount = 5
optionCount = len(select.options)

if expectedCount == optionCount:
    print("count is correct")
else:
    print("count is incorrect")



# ---------------------------------
# there ways to select the dropdown options value
# select the value by visible text
# select the value by Index
# select the value by using a value

# select.select_by_visible_text("Option 2")
# select.select_by_index(1)
# select.select_by_value("2")

# --------------------------------
targetedOption = 'Option 2'

for option in select.options:
    if option.text == targetedOption:
        option.click()
        print(f"Selected option is '{targetedOption}'")
        break
    else:
        print(f"option '{targetedOption}' is not found")


time.sleep(10)