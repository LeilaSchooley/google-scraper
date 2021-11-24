from selenium import webdriver
driver = webdriver.Firefox(executable_path="../Downloads/geckodriver")
driver.get("https://google.com/")