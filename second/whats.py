from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import time
import timeit
import threading
from urllib.parse import quote, urlencode
import pandas as pd
import numpy as np

# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    options=webdriver.ChromeOptions()
# )

# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    options=webdriver.FirefoxOptions()
# )


text = "The 2023 warnings from a renowned prophetess  warning about Tinubu's deception and desperation, begging her followers to free themselves from the political bondage of the APC. One year after, her prophesies are coming to pass and the people are in pain and anguish. May God hear the cry of His children and deliver us. amen                                                                                                     #Ekowa #OmoluabiEko #OurLagos                                                                                                 https://youtu.be/WOONBy6_dN0?si=TNpg_zyM2GugHrBd."


status = []


# df = pd.read_csv("contacts.csv")
# contacts_all = df["Name"].tolist()
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

# print(df_all)

# drivers = [driver1, driver2]

def send_bulk_msg(driver, contacts):
    for contact in contacts:
        print(f"Starting: {contact}")
        send_msg_to_contact(driver, contact)


def send_msg_to_contact(driver, contact):
    input_box_path = "#side > div._ak9t > div > div._ai04 > div._ai05 > div > div > p"
    input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=input_box_path))
        
    actions = ActionChains(driver)
    actions.click(input_box_search).perform()
    actions.send_keys(contact).perform()

    # print("Found the Search Box!")
    time.sleep(0.5)
    driver.find_element(by=By.CSS_SELECTOR, value=input_box_path).clear()
    input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=input_box_path))
        
    actions = ActionChains(driver)
    actions.click(input_box_search).perform()
    actions.send_keys(contact).perform()

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
        status.append("Not Sent")

    time.sleep(0.5)



# df["Status"] = status
# df.to_csv("status.csv", index=False)


# if __name__ == "__main__":
#     # Create threads
#     thread1 = threading.Thread(target=send_bulk_msg(drivers[0], df_all[0]))
#     thread2 = threading.Thread(target=send_bulk_msg(drivers[1], df_all[1]))

#     # Start threads
#     thread1.start()
#     thread2.start()

#     while True:
#         time.sleep(1)



df = pd.read_csv("contacts.csv")
contacts_all = df["Name"].tolist()
print("Gotten the names")
# Determine the number of rows in each split
num_rows = len(df["Name"])
split_size = num_rows // 2

# Split the DataFrame into 4 parts
dfs = np.array_split(df, 2)


def test_one():
    new_package = dfs[0]["Name"]
    
    driver1 = webdriver.Chrome()
    driver1.maximize_window()

    
    driver1.get("https://web.whatsapp.com")
    print("Scan QR Code for Driver 1, And then Enter")
    time.sleep(100)
    print("Logged In")

    send_bulk_msg(driver1, new_package.tolist())
    assert True

def test_two():
    new_package2 = dfs[1]["Name"]
    
    driver2 = webdriver.Edge()
    driver2.maximize_window()

    driver2.get("https://web.whatsapp.com")
    print("Scan QR Code for Driver 2, And then Enter")
    time.sleep(100)
    print("Logged In")
    send_bulk_msg(driver2, new_package2.tolist())

    assert True
