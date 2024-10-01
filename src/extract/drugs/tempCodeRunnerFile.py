import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tempstore import Drugs
import pandas as pd

# Webdriver, using firefox, at least its not edge
driver = webdriver.Firefox()

# Nafdac web scraping
url_nafdac = 'https://greenbook.nafdac.gov.ng/'

# Opens site
driver.get(url_nafdac)

# id is not available, so i am using the xpath to search
xpath_xpath = "/html/body/main/div/section/div/div[2]/div[1]/div[2]/div/label/input"
search_nafdac = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, xpath_xpath))
)

driver.find_element(By.XPATH, xpath_xpath)

# Automate it to be the two drugs
# First: create an iteration
# Second: using the dictionary key, search what drug would be searched first
# Third: NFD0001 table would be filled with Show 
# Product Name	Active Ingredients	NRN	Form	ROA	Strengths	Applicant Name	Approval Date	Status

# Column 
table_name = 'Nfd_001'
drug_cols = []
drug_data_df = pd.DataFrame(columns=drug_cols)
table_column = driver.find_elements(By.TAG_NAME, 'th')
for col in table_column:
    column_name = col.text.strip()
    drug_cols.append(column_name)

print(drug_cols)

# Rows
for drug in Drugs:
   for drug in Drugs:
    # Initial search
    search_nafdac.clear()
    search_nafdac.send_keys(drug)
    search_nafdac.send_keys(Keys.RETURN)
    time.sleep(5)

    # Dealing with medication rows
    while True:
        table_drug = driver.find_element(By.ID, 'DataTables_Table_0')
        table_rows = driver.find_elements(By.TAG_NAME, 'tr')

        for row in table_rows:
            columns = row.find_elements(By.TAG_NAME, 'td')
            row_data = [col.text for col in columns]

            # Append to DataFrame
            if len(row_data) == len(drug_cols):
                temp_df = pd.DataFrame([row_data], columns=drug_cols)
                drug_data_df = pd.concat([drug_data_df, temp_df], ignore_index=True)

     # Check for the next button
        try:
            next_button = driver.find_element(By.XPATH, '/html/body/main/div/section/div/div[2]/div[3]/div[2]/div/ul/li[6]/a')

            if 'disabled' in next_button.get_attribute('class'):
                break
            next_button.click()
            time.sleep(5)
        except Exception as e:
            print(f'Something happened: {str(e)}')
            break

driver.quit()
print(drug_data_df.head())