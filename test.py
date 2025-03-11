from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://rudra.devmat.in')
browser.maximize_window()

title = browser.title
print(title)
assert "Rudraksh padhyay" in title 