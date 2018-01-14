from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://www.python.org')

browser.close()
