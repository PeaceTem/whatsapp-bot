from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import time
from urllib.parse import quote, urlencode
import pandas as pd

text = "Hey, this message was sent using Selenium"
# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
driver = Remote(command_executor='http://127.0.0.1:4445/wd/hub', options=options)
driver.maximize_window()
print("Starting!")

driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
time.sleep(70)
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
        # status.append("Sent")

    except NoSuchElementException:
        back_path = "#side > div._ak9t > div > div._ai04 > button > div._ah_x._ai09 > span"
        back = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=back_path))
        print("Found no results!")
        ActionChains(driver).click(back).perform()
        # status.append("Not Sent")

    time.sleep(0.1)



df = pd.read_csv("contacts.csv")
contacts = df["Name"].tolist()

for contact in contacts:
    print(f"Starting: {contact}")

    send_msg_to_contact(contact)
    time.sleep(5)

print("Done")
# df["Status"] = status
# df.to_csv("status.csv", index=False)
time.sleep(180)
driver.quit()


