from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Webdriver, using firefox, at least its not edge
driver = webdriver.Firefox()

# Nafdac web scraping
url_nafdac = 'https://greenbook.nafdac.gov.ng/'

# Opens site
driver.get(url_nafdac)

# id is not available, so i am using the xpath to search
xpath_xpath = "/html/body/main/div/section/div/div[1]/div[2]/div/label/input"
search_nafdac = driver.find_element(By.XPATH, xpath_xpath)

# Automate it to be the two drugs
# First: create an iteration
# Second: using the dictionary key, search what drug would be searched first
# Third: NFD0001 table would be filled with Show 
# Product Name	Active Ingredients	NRN	Form	ROA	Strengths	Applicant Name	Approval Date	Status

