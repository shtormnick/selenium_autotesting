from selenium import webdriver
from selenium.webdriver.support.ui import Select 
import math
import time 

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    int1 = browser.find_element_by_id("num1")
    int1_1 = int(int1.text)
    int2 = browser.find_element_by_id("num2")
    int2_2 = int(int2.text)

    result = int1_1 + int2_2
    result_str = str(result)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(result_str)

    browser.find_element_by_css_selector("button.btn").click()

    
    

finally:
    time.sleep(10)
    browser.quit()