from selenium import webdriver
import math 
import time
import os 

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firs_name = browser.find_element_by_name("firstname")
    firs_name.send_keys("SSSSs")
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("SSSSsss")
    email = browser.find_element_by_name("email")
    email.send_keys("Wasd@asd.asd")

    file = browser.find_element_by_id("file")
    file.send_keys(file_path)

    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()
    
finally:
    time.sleep(10)
    browser.quit()