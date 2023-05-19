from robotics import Robot


SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")

def introduce_yourself():
    robot.say_hello()
    print('\n')
    print('I am going to use Selenium RPA to navigate through Wikipedia and grap information about 4 different scientist.')
    print('Their date of birth, death and age. And will also dispay a short summary')
    print('Hope you find the provided information useful')

def navigate_to_wikipedia():
    robot.open_webpage('https://en.wikipedia.org/wiki/Main_Page')

def search_for_scientist(text):
    robot.get_scientist_page(text)

def print_date_of_birth_death(scientist):
    robot.get_birth_death_dates(scientist)

def print_summary(scientist):
    robot.get_scientist_summary(scientist)

def excuse_yourself():
    robot.say_goodbye()

def print_scientist_info(scientist):

    print('\n')
    print('Scientist name: ' + scientist)
    print('-------')
    navigate_to_wikipedia()
    search_for_scientist(scientist)
    print_date_of_birth_death(scientist)
    print('-------') 
    print('Summary:') 
    print_summary(scientist)
    print('\n')
def main():
    introduce_yourself()

    for item in SCIENTISTS:
        print_scientist_info(item)

    excuse_yourself()

if __name__ == "__main__":
    main()