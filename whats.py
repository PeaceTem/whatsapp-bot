from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import multiprocessing
import os
import time
import timeit
import threading
from urllib.parse import quote, urlencode
import pandas as pd
import numpy as np

# USE SELENIUM STANDALONE CONTAINERS TO RUN
# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4445/wd/hub',
#    options=webdriver.ChromeOptions()
# )



text = "The 2023 warnings from a renowned prophetess  warning about Tinubu's deception and desperation, begging her followers to free themselves from the political bondage of the APC. One year after, her prophesies are coming to pass and the people are in pain and anguish. May God hear the cry of His children and deliver us. amen                                                                                                     #Ekowa #OmoluabiEko #OurLagos                                                                                                 https://youtu.be/WOONBy6_dN0?si=TNpg_zyM2GugHrBd."

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://web.whatsapp.com")
print("Scan QR Code for Driver 1, And then Enter")
time.sleep(200)
print("Logged In")

status = []



df = pd.read_csv("new_contacts.csv")

df.drop_duplicates()
dfs = np.array_split(df, 2)
contacts = dfs[0]["Name"].tolist()
# print("Gotten the names")
# # Determine the number of rows in each split
# num_rows = len(df["Name"])
# split_size = num_rows // 2

# # Split the DataFrame into 4 parts
# dfs = np.array_split(df, 2)
# # print(dfs)
# df_all = []
# for df in dfs:
#     print(df["Name"].tolist())
#     df_all.append(df["Name"].tolist())

# # print(df_all)



def send_msg_to_contact(contact):
    input_box_path = "#side > div._ak9t > div > div._ai04 > div._ai05 > div > div > p"
    input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=input_box_path))
        
    actions = ActionChains(driver)
    actions.click(input_box_search).perform()
    actions.send_keys(contact).perform()
    # print("Found the Search Box!")
    time.sleep(0.2)
    try:
        selected_contact = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.XPATH, value="//span[@title='"+contact+"']"))
        selected_contact.click()
        ActionChains(driver).send_keys(text + Keys.ENTER).perform()
        # status.append("Sent")

    except NoSuchElementException:
        back_path = "#side > div._ak9t > div > div._ai04 > button > div._ah_x._ai09 > span"
        back = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=back_path))
        # print("Found no results!")
        ActionChains(driver).click(back).perform()
        # status.append("Not Sent")

    time.sleep(0.2)





# def send_bulk_msg(driver, contacts):
for contact in contacts:
    print(f"Starting: {contact}")
    send_msg_to_contact(contact)


time.sleep(999999)

# def send_bulk_msg2(driver, contacts):
#     for contact in contacts:
#         print(f"Starting: {contact}")
#         send_msg_to_contact2(driver, contact)


# def send_msg_to_contact2(driver, contact):
#     input_box_path = "#side > div._ak9t > div > div._ai04 > div._ai05 > div > div > p"
#     input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=input_box_path))
        
#     actions = ActionChains(driver)
#     actions.click(input_box_search).perform()
#     actions.send_keys(contact).perform()
#     # print("Found the Search Box!")
#     time.sleep(0.5)
#     try:
#         selected_contact = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.XPATH, value="//span[@title='"+contact+"']"))
#         selected_contact.click()
#         ActionChains(driver).send_keys(text + Keys.ENTER).perform()
#         # status.append("Sent")

#     except NoSuchElementException:
#         back_path = "#side > div._ak9t > div > div._ai04 > button > div._ah_x._ai09 > span"
#         back = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=back_path))
#         # print("Found no results!")
#         ActionChains(driver).click(back).perform()
#         # status.append("Not Sent")

#     time.sleep(0.5)



# if __name__ == "__main__":
#     processes = []
#     args_list = [0, 1]  # Example list of arguments
    
#     # Create 4 processes, each running the function with a different argument
#     for arg in args_list:
#         process = multiprocessing.Process(target=send_bulk_msg, args=(drivers[arg], df_all[arg]))
#         processes.append(process)
#         process.start()
    
#     # Wait for all processes to finish
#     for process in processes:
#         process.join()


# df["Status"] = status
# df.to_csv("status.csv", index=False)


# if __name__ == "__main__":
#     # Create threads
#     thread1 = threading.Thread(target=send_bulk_msg(drivers[0], df_all[0]))
#     thread2 = threading.Thread(target=send_bulk_msg2(drivers[1], df_all[1]))

#     # Start threads
#     thread1.start()
#     thread2.start()

#     while True:
#         time.sleep(1)
driver.quit()
