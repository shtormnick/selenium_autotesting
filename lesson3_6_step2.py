from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest 
import math 
import time


@pytest.mark.parametrize("link", [("https://stepik.org/lesson/236895/step/1"),
("https://stepik.org/lesson/236896/step/1"),
("https://stepik.org/lesson/236897/step/1"),
("https://stepik.org/lesson/236898/step/1"),
("https://stepik.org/lesson/236899/step/1"),
("https://stepik.org/lesson/236903/step/1"),
("https://stepik.org/lesson/236904/step/1"),
("https://stepik.org/lesson/236905/step/1")])
def test_main(link):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        answer = math.log(int(time.time()))
        str_answert = str(answer)
        
        input_answer = browser.find_element_by_css_selector(".textarea")
        input_answer.send_keys(str_answert)
        submit= browser.find_element_by_class_name("submit-submission")
        submit.click()

        correct = browser.find_element_by_class_name("smart-hints__hint").text
        assert correct == "Correct!" , "something wrong with correct field"

    finally:
        time.sleep(5)
        browser.quit()