from RPA.Browser.Selenium import Selenium

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import StaleElementReferenceException

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


        # try:
        # input_element = driver.find_element_by_name('search')

        input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "search")))
        
        try:
            input_element.send_keys(text)
        except StaleElementReferenceException:
            input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "search")))
            input_element.send_keys(text)

        

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cdx-button"))
        ).click()

        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "mw-search-result-ns-0"))
        # ).click()

        # finally:
        #     driver.quit()


        # input_element = driver.find_element_by_name('search')

        # input_element.send_keys(text)

        # input_element.send_keys(Keys.ENTER)


        # first_search_result = driver.find_element_by_class_name('mw-search-result-ns-0')

        # first_search_result.find_element_by_tag_name('a').click()


    def get_birth_death_dates(self, scientist):
        
        info_card = driver.find_element_by_class_name('infobox')  

        dates = info_card.find_elements_by_class_name('infobox-data')

        birthdate_text = dates[0].text

        birthdate_year = ''

        if scientist == "Marie Curie" or  scientist == "Charles Darwin":
            birthdate_year = int(birthdate_text.split(" ")[4].split('\n')[0])
        else:
            birthdate_year = int(birthdate_text.split(" ")[2].split('\n')[0])

        deathdate_text = dates[1].text

        deathdate_year = int(deathdate_text.split(" ")[2])

        age_at_death = deathdate_year - birthdate_year

        print(scientist + " was born in the year " + str(birthdate_year) + " and died in the year " + str(deathdate_year) + " at the age of " + str(age_at_death) + ".")


    def get_scientist_summary(self, scientist):
        

        if scientist == "Marie Curie":

            body_content = driver.find_element_by_id('mw-content-text')

            first_paragraph = body_content.find_element_by_xpath("//p[3]")

            print(first_paragraph.text)

        else:

            body_content = driver.find_element_by_id('mw-content-text')

            first_paragraph = body_content.find_element_by_xpath("//p[2]")

            print(first_paragraph.text)
