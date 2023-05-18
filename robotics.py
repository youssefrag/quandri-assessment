from RPA.Browser.Selenium import Selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is " + self.name)

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def open_webpage(self, webpage):
        driver.get(webpage)

    def get_scientist_page(self, text):

        input_element = driver.find_element_by_name('search')

        print(input_element.tag_name)

        input_element.send_keys(text)

        input_element.send_keys(Keys.ENTER)

        first_search_result = driver.find_element_by_class_name('mw-search-result-ns-0')

        print(first_search_result.tag_name)

        search_result_heading = first_search_result.find_element_by_tag_name('a').click()

        