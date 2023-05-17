from RPA.Browser.Selenium import Selenium

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

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

    def add_to_search_field(self, text):

        input_element = driver.find_element_by_name('search')

        print(input_element.tag_name)

        