
from time import sleep
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Scraper():

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="./geckodriver")
        self.driver.implicitly_wait(7)
        self.vars = {}

    def random_sleep(self):
        sleep(random.randint(1,4))

    def sleep_click(self, element):
        sleep(random.randint(1,4))
        element.click()

    def slow_type(self, element, text, delay=0.1):
        """Send a text to an element one character at a time with a delay."""
        for character in text:
            element.send_keys(character)
            time.sleep(delay)

    def test_google(self):

        try:
            self.driver.get("https://www.google.com/")
            self.driver.set_window_size(1608, 1023)
            element = self.driver.find_element(By.XPATH,
                                     "/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/button[2]/div")

            self.sleep_click(element)
            self.driver.find_element(By.NAME, "q").click()

            element = self.driver.find_element(By.NAME, "q")

            self.slow_type(element, "restaurants in east london")
            element = self.driver.find_element(
                By.XPATH, "(//input[@name=\'btnK\'])[2]")

            self.sleep_click(element)

        except Exception as e:
            print(e)
            self.driver.quit()


bot = Scraper()
bot.test_google()
