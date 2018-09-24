#========================================================================================
# - Scrap the javascript site 
#========================================================================================
import csv
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.applebees.com/en/locations")

elem = driver.find_element_by_id("location-search-input")

elem.send_keys("Gujrat,India" + Keys.RETURN)
time.sleep(3)
elem = driver.find_element_by_class_name("c-location-input__action").click()

