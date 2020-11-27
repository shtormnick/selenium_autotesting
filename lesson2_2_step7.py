from selenium import webdriver
import math
import time 

link = "http://suninjuly.github.io/execute_script.html"

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
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_box)
    check_box.click()
    radio_box = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_box)
    radio_box.click()

    submit = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()


finally:
    time.sleep(10)
    browser.quit()    