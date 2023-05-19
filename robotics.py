from RPA.Browser.Selenium import Selenium

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    # function to open wikipedia webpage
    def open_webpage(self, webpage):
        driver.get(webpage)

    # find the page for each specific scientist
    def get_scientist_page(self, text):

        # find the seatch box to enter scientist name
        input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "search")))
        
        # error handling in case a stale element error comes up
        try:
            # if there is no error, send the scientist name to the search field
            input_element.send_keys(text)

        except StaleElementReferenceException:
            # in case a stale element error happens, redo the search for the search field
            input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "search")))
            # send keys to field
            input_element.send_keys(text)

        # wait until search button is located and then click to search for scientist
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cdx-button"))
        ).click()


    # function to get birth and death dates
    def get_birth_death_dates(self, scientist):
        
        # find dates on page using the classnames of their containing elements
        info_card = driver.find_element_by_class_name('infobox')  
        dates = info_card.find_elements_by_class_name('infobox-data')

        # list containing birth and death dates. Extract birth date as first item of list
        birthdate_text = dates[0].text

        birthdate_year = ''

        # Two scientists' birth dates were positioned differently in birthdate text
        # After splitting text into a list, grab the item containing the year and turn into integer
        if scientist == "Marie Curie" or  scientist == "Charles Darwin":
            birthdate_year = int(birthdate_text.split(" ")[4].split('\n')[0])
        else:
            birthdate_year = int(birthdate_text.split(" ")[2].split('\n')[0])


        # list containing birth and death dates. Extract death date as second item of list
        deathdate_text = dates[1].text

        # split text into list, extract death date and turn into integer
        deathdate_year = int(deathdate_text.split(" ")[2])

        # calculate age at death
        age_at_death = deathdate_year - birthdate_year

        # print to console information on birth/death dates and age
        print(scientist + " was born in the year " + str(birthdate_year) + " and died in the year " + str(deathdate_year) + " at the age of " + str(age_at_death) + ".")


    # Get first paragraph of wikipedia page for each scientist
    def get_scientist_summary(self, scientist):
        
        # Element layout for Marie Curie page is different so if statement needed to account for difference

        if scientist == "Marie Curie":

            # Find first paragraph
            body_content = driver.find_element_by_id('mw-content-text')
            first_paragraph = body_content.find_element_by_xpath("//p[3]")

            print(first_paragraph.text)

        else:
            
            # Find first paragraph
            body_content = driver.find_element_by_id('mw-content-text')
            first_paragraph = body_content.find_element_by_xpath("//p[2]")

            print(first_paragraph.text)
