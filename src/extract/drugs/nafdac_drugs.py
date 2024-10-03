import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from tempstore import Drugs

# Initialize WebDriver (using Firefox)
driver = webdriver.Firefox()

# Open NAFDAC website
url_nafdac = 'https://greenbook.nafdac.gov.ng/'
driver.get(url_nafdac)

# ID for search box
search_id = "search_product"
search_nafdac = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, search_id))
)

# Initialize dataframe
drug_cols = []
drug_data_df = pd.DataFrame(columns=drug_cols)

# Get table columns
table_column = driver.find_elements(By.TAG_NAME, 'th')
for col in table_column:
    column_name = col.text.strip()
    drug_cols.append(column_name)

print(drug_cols)

# Loop through each drug and search
for drug in Drugs.keys():  
    
    # Scroll to search box to ensure it is in view
    driver.execute_script("arguments[0].scrollIntoView();", search_nafdac)
    time.sleep(1)  

    # Search for drug
    search_nafdac.clear()
    search_nafdac.send_keys(drug)
    search_nafdac.send_keys(Keys.RETURN)
    time.sleep(5)

    # Scrape rows
    while True:
        try:
            table_rows = driver.find_elements(By.TAG_NAME, 'tr')
            for row in table_rows:
                columns = row.find_elements(By.TAG_NAME, 'td')
                row_data = [col.text if col.text else None for col in columns]

                # Append to DataFrame if row_data matches column count
                if len(row_data) == len(drug_cols):
                    temp_df = pd.DataFrame([row_data], columns=drug_cols)
                    drug_data_df = pd.concat([drug_data_df, temp_df], ignore_index=True)

            # Check for the "Next" button and handle pagination
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Next'))
            )
            driver.execute_script("arguments[0].scrollIntoView();", next_button)
            time.sleep(1) 
            if 'disabled' in next_button.get_attribute('class'):
                break
            next_button.click()
            time.sleep(5) 

        except Exception as e:
            print(f'Something happened while scraping: {str(e)}')
            break

# Close the driver
driver.quit()

# Fill missing values with 'N/A' and save to CSV
drug_data_df.fillna('N/A', inplace=True)
print(drug_data_df.head())
drug_data_df.to_csv('drug_data_Nf.csv', index=False)
