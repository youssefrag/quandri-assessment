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

        input_element.send_keys(text)

        driver.implicitly_wait(1000000000)

        driver.find_element_by_name('search').send_keys(Keys.ENTER)

        # for x in range(0, 3):

        #     try:
        #         driver.find_element_by_name('search').send_keys(Keys.ENTER)
        #         break
        #     except:
        #         print('exception occured, trying again')


        first_search_result = driver.find_element_by_class_name('mw-search-result-ns-0')


        first_search_result.find_element_by_tag_name('a').click()


    def get_birth_death_dates(self, scientist):
        
        info_card = driver.find_element_by_class_name('infobox')  

        dates = info_card.find_elements_by_class_name('infobox-data')

        birthdate_text = dates[0].text

        # print(birthdate_text)

        # print(birthdate_text.split(" "))

        birthdate_year = ''

        if scientist == "Marie Curie" or  scientist == "Charles Darwin":
            birthdate_year = int(birthdate_text.split(" ")[4].split('\n')[0])
        else:
            birthdate_year = int(birthdate_text.split(" ")[2].split('\n')[0])

        # birthdate_year = int(birthdate_text.split(" ")[2].split('\n')[0])

        print(birthdate_year)

        # print(dates[1].text)

        deathdate_text = dates[1].text

        # print(deathdate_text)

        deathdate_year = int(deathdate_text.split(" ")[2])

        print(deathdate_year)

        age_at_death = deathdate_year - birthdate_year

        print(age_at_death)