from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import time
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
time.sleep(55.5)
print("Logged In")


status = []
def send_msg_to_contact(contact):
    input_box_path = "#side > div._ak9t > div > div._ai04 > div._ai05 > div > div > p"
    input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=input_box_path))
        
    actions = ActionChains(driver)
    actions.click(input_box_search)
    actions.send_keys(contact)
    actions.perform()
    print("Found the Search Box!")
    time.sleep(0.1)
    try:
        selected_contact = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.XPATH, value="//span[@title='"+contact+"']"))
        selected_contact.click()
        actions2 = ActionChains(driver)
        actions2.send_keys(text + Keys.ENTER)
        actions2.perform()
        status.append("Sent")

    except NoSuchElementException:
        back_path = "#side > div._ak9t > div > div._ai04 > button > div._ah_x._ai09 > span"
        back = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=back_path))
        print("Found no results!")
        ActionChains(driver).click(back).perform()
        status.append("Not Sent")

    time.sleep(1)



df = pd.read_csv("contacts.csv")
contacts = df["Name"].tolist()

# contacts = ["pa pa pa kilode", "Pa Olugbongaga Factorial", "Pa Olugbongaga Factorial 2"]
for contact in contacts:
    send_msg_to_contact(contact)

# send_msg_to_contact("pa pa pa kilode")

df["Status"] = status
df.to_csv("status.csv", index=False)
time.sleep(180)
driver.quit()


# research more about selenium grid
# learn how to use windows remote connection
# use flutter to get the contacts on phone and send a message template to all of them
# learn how to use docker



# class WhatsApp:
#     def


# use flutter to send messages to multiple people at once
# get contacts list on a particular phone
# insert as many as possible numbers to a phone's contacts list
# upload a csv file that contains the phone numbers and save them
# you can also add delete function to it.
# Basically, you can create your own Contact app with a new design and upload it to google playstore
# Octave go pay for your playstore account