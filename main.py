from turtle import clear
from robotics import Robot


SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()

def navigate_to_wikipedia():
    robot.open_webpage('https://en.wikipedia.org/wiki/Main_Page')

def search_for_scientist(text):
    robot.get_scientist_page(text)

def excuse_yourself():
    robot.say_goodbye()


def main():
    introduce_yourself()
    navigate_to_wikipedia()
    search_for_scientist("Albert Einstein")


if __name__ == "__main__":
    main()
