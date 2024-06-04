from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
# from selenium import webdriver

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
# driver = webdriver.Chrome()

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
time.sleep(80)
print("Logged In")

# input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value="#side > div._ak9t > div > div._ai04 > div._ai05 > div > div > p"))
status = []
def send_msg_to_contact(contact):
    input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value="#side > div._ak9t > div > div._ai04 > div._ai05 > div > div > p"))
        
    actions = ActionChains(driver)
    actions.click(input_box_search)
    actions.send_keys(contact)
    actions.perform()
    print("Found the Search Box!")
    time.sleep(2)
    try:
        selected_contact = driver.find_element(by=By.XPATH, value="//span[@title='"+contact+"']")
        selected_contact.click()
        actions2 = ActionChains(driver)
        actions.send_keys(text + Keys.ENTER)
        actions.perform()
        status.append("Sent")
    except NoSuchElementException:
        time.sleep(1)
        back_path = "#side > div._ak9t > div > div._ai04 > button > div._ah_x._ai09 > span"
        # no_results_path = "#pane-side > div > div > span"
        no_results = driver.find_element(by=By.CSS_SELECTOR, value=back_path)
        print("Found no results!")
        
        ActionChains(driver).click(no_results).perform()
        status.append("Not Sent")

        # # Opens a new tab and switches to new tab
        # # driver.switch_to.new_window('tab')
            
        # # Setup wait for later
        # print("Sleeping!")
        # time.sleep(20)
        # wait = WebDriverWait(driver, 10)

        # # Query parameters
        # params = {
        #     'phone': '+2349164702871',
        #     'text': 'jksdfghjkgks'
        # }
        
        # # Encode query parameters
        # query_string = urlencode(params)
        # base_url = "https://web.whatsapp.com/send"
        # # Construct the full URL
        # full_url = f"{base_url}?{query_string}"

        # driver.get(full_url)
        # print("New Tab!")

        # time.sleep(80)
        # wait = WebDriverWait(driver, 80)
        # print("New Chat!")

        # inp_xpath = '#main > footer > div._ak1k._ahmw.copyable-area > div > span:nth-child(2) > div > div._ak1r > div._ak1l > div > div.x1hx0egp.x6ikm8r.x1odjw0f.x1k6rcq7.x6prxxf > p'
        # input_box = driver.find_element(by=By.CSS_SELECTOR, value=inp_xpath)

        # print("Found the contact!")

        # ActionChains(driver).move_to_element(input_box).send_keys(Keys.ENTER).perform()
        # print("The enter key has been clicked!")
        # time.sleep(10)

    # inp_xpath = '#main > footer > div._ak1k._ahmw.copyable-area > div > span:nth-child(2) > div > div._ak1r > div._ak1l > div > div.x1hx0egp.x6ikm8r.x1odjw0f.x1k6rcq7.x6prxxf > p'
    # input_box = driver.find_element(by=By.CSS_SELECTOR, value=inp_xpath)
    # time.sleep(2)
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