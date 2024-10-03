import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tempstore import Drugs
import time

# Webdriver, using Firefox
driver = webdriver.Firefox()

# Save Drugs.com site url
url_drugsdotcom = 'https://www.drugs.com/drug_information.html'

# Opens site
driver.get(url_drugsdotcom)

def drug_nav(drug_name, letter_count):
    '''write the doc'''
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'ul li a.ddc-paging-item')))    
    letter = lambda x : drug_name[letter_count].upper() if letter_count == 0 else drug_name[ : letter_count].capitalize()
    xpath = f"//a[@class='ddc-paging-item' and text()='{letter(letter_count)}']"
    letter_link = driver.find_element(By.XPATH, xpath)
    letter_link.click()
    # Navigate to the page of the drug to scrape
    xpath = f"//a[@class='nav-item' and text()='Professional Monographs']"
    path_link = driver.find_element(By.XPATH, xpath)
    path_link.click()
    # Click the variant link
    ul_variant_element = driver.find_element(By.CLASS_NAME, 'ddc-list-column-2')
    li_elements = ul_variant_element.find_elements(By.TAG_NAME, 'li')
    for li in li_elements :
        variant_link = li.find_element(By.TAG_NAME, 'a')
        if variant_link.text.lower() == drug_name.lower():
            variant_link.click()
            scrape_variant_data()
            return None


def scrape_variant_data():
    print("hello")
    return None




for key, variants in Drugs.items():
    key_drug = key


    try:
        drug_name = key_drug
        drug_nav(key_drug,0) 
        for variant in variants:
            drug_name = variant
            drug_nav(variant,2)
            driver.back()
        driver.back()
        
    
    except Exception as e:
        print(f"An error occurred while searching for {drug_name}: {e}")

# Don't forget to close the browser when you're done
#driver.close()