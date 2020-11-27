from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/math.html"
def  calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click
    radio_box = browser.find_element_by_id("robotsRule")
    radio_box.click

    submit = browser.find_element_by_css_selector("button.btn")


finally:
    time.sleep(15)
    browser.quit()
