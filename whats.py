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
from urllib.parse import quote, urlencode
import pandas as pd

# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    options=webdriver.ChromeOptions()
# )

# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    options=webdriver.FirefoxOptions()
# )


text = "Hey, this message was sent using Selenium"

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
time.sleep(50)
print("Logged In")

status = []
def send_msg_to_contact(contact):
    input_box_path = "#side > div._ak9t > div > div._ai04 > div._ai05 > div > div > p"
    input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=input_box_path))
        
    ActionChains(driver).click(input_box_search).send_keys(contact).perform()
    # print("Found the Search Box!")
    time.sleep(0.3)
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

    time.sleep(0.1)


df = pd.read_csv("contacts.csv")
contacts = df["Name"].tolist()
print("Gotten the names")

# def send_bulk_msg():
for contact in contacts:
    send_msg_to_contact(contact)




# # Measure the execution time of example_function
# execution_time = timeit.timeit("send_bulk_msg()", setup="from __main__ import send_bulk_msg", number=1)
# print("Doing the timing job")
# print(f"Execution time: {execution_time / 30} seconds per call")


# df["Status"] = status
# df.to_csv("status.csv", index=False)
time.sleep(180)
driver.quit()


# research more about selenium grid
# learn how to use windows remote connection
# use flutter to get the contacts on phone and send a message template to all of them
# learn how to use docker

# use flutter to send messages to multiple people at once
# get contacts list on a particular phone
# insert as many as possible numbers to a phone's contacts list
# upload a csv file that contains the phone numbers and save them
# you can also add delete function to it.
# Basically, you can create your own Contact app with a new design and upload it to google playstore
# Octave go pay for your playstore account

