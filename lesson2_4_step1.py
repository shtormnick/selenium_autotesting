from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"


def submit_btn():
    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    submit_btn()

    alert = browser.switch_to_alert()
    alert.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    submit_btn()

finally:
    time.sleep(5)
    browser.quit()