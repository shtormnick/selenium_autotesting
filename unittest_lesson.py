import unittest
from selenium import webdriver
import math 
import time

class Tests(unittest.TestCase):

    def test_abs1(self):

        link = "http://suninjuly.github.io/registration1.html"

        try:
            browser = webdriver.Chrome() 
            browser.get(link)

            input1 = browser.find_element_by_tag_name("input.first")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_tag_name("input.second")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_tag_name("input.third")
            input3.send_keys("sss@sss.ss")
            input4 = browser.find_element_by_tag_name("div.second_block input.first")
            input4.send_keys("+380999999999")
            input5 = browser.find_element_by_tag_name("div.second_block input.second")
            input5.send_keys("Russia")
            button = browser.find_element_by_xpath("//button[@type='submit']")
            button.click()

        finally:
            time.sleep(15)
            browser.quit()

    def test_abs2(self):

        link = "http://suninjuly.github.io/registration2.html"

        try:
            browser = webdriver.Chrome() 
            browser.get(link)

            input1 = browser.find_element_by_tag_name("input.first")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_class_name("input.third")
            input2.send_keys("sss@sss.ss")
            input3 = browser.find_element_by_class_name("div.second_block input.first")
            input3.send_keys("+380999999999")
            input4 = browser.find_element_by_id("div.second_block input.second")
            input4.send_keys("Russia")
            button = browser.find_element_by_xpath("//button[@type='submit']")
            button.click()

        finally:
            time.sleep(15)
            browser.quit()
            
if __name__ == "__main__":
    unittest.main()