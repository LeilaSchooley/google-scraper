from time import sleep
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

class Scraper():

    def __init__(self):
        #self.driver = webdriver.Firefox(executable_path="/usr/local/geckodriver")
        #self.driver.implicitly_wait(7)
        self.vars = {}

    def random_sleep(self):
        sleep(random.randint(1, 4))

    def sleep_click(self, element):
        try:
            sleep(random.randint(1, 4))
            element.click()
        except Exception as e:
            print(e)
            pass
    def slow_type(self, element, text, delay=0.1):
        """Send a text to an element one character at a time with a delay."""
        for character in text:
            element.send_keys(character)
            time.sleep(delay)

    def create_letter_document(self):
        pass
    def quit_browser(self):
        print("Quitting in 3 seconds")
        sleep(3)
        self.driver.quit()

    def test_google(self):


        self.driver.get("https://www.google.com/")
        self.driver.set_window_size(1608, 1023)
        #element = self.driver.find_element(By.XPATH,
        #                                   "/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/button[2]/div")
#
        #self.sleep_click(element)
        self.driver.find_element(By.NAME, "q").click()

        element = self.driver.find_element(By.NAME, "q")

        self.slow_type(element, "restaurants in east london\n")
        element = self.driver.find_element(
            By.XPATH, "(//input[@name=\'btnK\'])[2]")

        self.sleep_click(element)

        element = self.driver.find_element(By.LINK_TEXT, "View all")
        self.sleep_click(element)

        sleep(4)
        element = self.driver.find_element(By.TAG_NAME, "body")

        print(        element.get_attribute('innerHTML'))
    def test_request(self):
        path_img ="../captcha.jpeg"
        url = ("http://localhost:5000/upload")
        with open(path_img, 'rb') as img:
            name_img = os.path.basename(path_img)
            files = {'image': (name_img, img, 'multipart/form-data', {'Expires': '0'})}
            with requests.Session() as s:
                r = s.post(url, files=files)
                print(r.status_code)
                print(r.text)

bot = Scraper()
bot.test_request()
