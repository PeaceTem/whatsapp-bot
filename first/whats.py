from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC

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


text1 = "The 2023 warnings from a renowned prophetess  warning about Tinubu's deception and desperation, begging her followers to free themselves from the political bondage of the APC. One year after, her prophesies are coming to pass and the people are in pain and anguish. May God hear the cry of His children and deliver us. amen"
text2 = "#Ekowa #OmoluabiEko #OurLagos"
text3 = "https://youtu.be/WOONBy6_dN0?si=TNpg_zyM2GugHrBd."
text = "                                                                          ".join([text1, text2, text3])
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://web.whatsapp.com")
# print("Scan QR Code for Driver 1, And then Enter")
# time.sleep(100)
# print("Logged In")

status = []



# df = pd.read_csv("new_contacts.csv")

# df.drop_duplicates()
# dfs = np.array_split(df, 2)
# contacts = dfs[0]["Name"].tolist()
def the_the():
    return 1
def send_bulk_msg(driver, contacts):
    for contact in contacts:
        print(f"Starting: {contact}")
        send_msg_to_contact(driver, contact)



def send_msg_to_contact(driver, contact):
    try:
        count = 0
        while count < 5: 
            search = "#side > div._ak9t > div > div._ai04 > button > div._ah_x._ai09 > span > svg"
            search = WebDriverWait(driver,5).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=search))
            ActionChains(driver).click(search).perform()
            confirmation_element = driver.find_element(by=By.CSS_SELECTOR, value="#side > div._ak9t > div > div._ai04 > button")
            label = confirmation_element.get_attribute("aria-label")
            print("Label", label, sep=", ")
            if label == "Search or start new chat":
                search = WebDriverWait(driver,5).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=search))
                ActionChains(driver).click(search).perform()

            elif label == "Chat list":
                break

            count += 1


        ActionChains(driver).send_keys(contact).perform()

    except:
        print(f"An exception occurred in the input box for {contact}")
        pass


    print("Found the Search Box!")
    try:
        # selected_contact = driver.find_element(by=By.XPATH, value="//span[@title='"+contact+"']")
        selected_contact_path = "//span[@title='"+contact+"']"
        selected_contact = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, selected_contact_path)))
        ActionChains(driver).click(selected_contact).perform()
        time.sleep(0.2)
        # text_box = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#main > footer > div._ak1k._ahmw.copyable-area > div > span > div > div._ak1r > div._ak1l > div > div.x1hx0egp.x6ikm8r.x1odjw0f.x1k6rcq7.x6prxxf > p")))
        ActionChains(driver).send_keys(text + Keys.ENTER).perform()


    except:
        print(f"An exception occurred in the input box for {contact}")
        # back_path = "#side > div._ak9t > div > div._ai04 > button > div._ah_x._ai09 > span > svg"
        # back = WebDriverWait(driver,5).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=back_path))
        # ActionChains(driver).click(back).perform()
        # time.sleep(0.2)

