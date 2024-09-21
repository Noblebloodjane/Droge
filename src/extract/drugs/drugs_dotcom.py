from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Webdriver, using firefox, at least its not edge
driver = webdriver.Firefox()

# Drugs.com web scraping
url_drugsdotcom = 'https://www.drugs.com/drug_information.html'

# Opens site
driver.get(url_drugsdotcom)

# Automate it to be the two drugs
# First: create an iteration
# Second: using the dictionary, and the first letter of that key pick which link to select first
# Third: using the dictionary, and first two letters of that key, pick the link
# Fourth: using the list, and string of that item, pick the link/drug
# Fifth: save the whole page and save the pages of links with the main word



# logic to be used
# i do not want to hard code
# hardcode first but create a table that stores drugs to be tracked which are Amoxicillin(common antibiotics) and 

