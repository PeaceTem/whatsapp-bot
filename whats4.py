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

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4445/wd/hub',
   options=webdriver.ChromeOptions()
)



text = "Hey, this message was sent using Selenium"

# driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://web.whatsapp.com")
print("Scan QR Code for Driver 1, And then Enter")
time.sleep(400)

print("Logged In")


status = []




df = pd.read_csv("new_contacts.csv")

df.drop_duplicates()
dfs = np.array_split(df, 4)
contacts = dfs[3]["Name"].tolist()
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
    time.sleep(1)
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

    time.sleep(1)





# def send_bulk_msg(driver, contacts):
for contact in contacts:
    print(f"Starting: {contact}")
    send_msg_to_contact(contact)


time.sleep(999999)
driver.quit()
