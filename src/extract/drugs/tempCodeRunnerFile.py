
# # Rows
# for drug in Drugs:
#     # Initial
#     search_nafdac.clear()
#     search_nafdac.send_keys(drug)
#     search_nafdac.send_keys(Keys.RETURN)
#     time.sleep(5)

#     # Dealing with medication rows
#     while True:
#         table_drug = driver.find_element(By.ID, 'DataTables_Table_0')
#         table_rows = driver.find_elements(By.TAG_NAME, 'tr')

#         for row in table_rows:
#             columns = row.find_elements(By.TAG_NAME, 'td')
           
#             print([col.text for col in columns])
#             try:
#                 next_button = driver.find_element(By.ID, 'dataTables_Table_0_next')

#                 if 'disabled' in next_button.get_attribute('class'):
#                     break
#                 next_button.click
#                 time.sleep(5)
#             except Exception as e:
#                 print(f'Something happened i can feel it : {str(e)}')
#                 break
        
