from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import time
from urllib.parse import quote, urlencode


# use this file to just open whatsapp and use click to chat direct
# 

driver = webdriver.Chrome()
driver.maximize_window()
text = "Hey, this message was sent using Selenium"

driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
time.sleep(80)
print("Logged In")


def send_msg_to_contact():
    # input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value="#side > div._ak9t > div > div._ai04 > div._ai05 > div > div > p"))
        
    # actions = ActionChains(driver)
    # actions.click(input_box_search)
    # actions.send_keys(contact)
    # actions.perform()
    # print("Found the Search Box!")



    # Query parameters
    params = {
        'phone': '+2349164702871',
        'text': 'jksdfghjkgks'
    }
    
    # Encode query parameters
    query_string = urlencode(params)
    base_url = "https://web.whatsapp.com/send"
    # Construct the full URL
    full_url = f"{base_url}?{query_string}"

    driver.get(full_url)
    print("New Tab!")

    time.sleep(100)
    inp_xpath = '#main > footer > div._ak1k._ahmw.copyable-area > div > span:nth-child(2) > div > div._ak1r > div._ak1l > div > div.x1hx0egp.x6ikm8r.x1odjw0f.x1k6rcq7.x6prxxf > p'
    input_box = driver.find_element(by=By.CSS_SELECTOR, value=inp_xpath)
    print("Found the contact!")

    ActionChains(driver).move_to_element(input_box).send_keys(Keys.ENTER).perform()
    print("The enter key has been clicked!")
    time.sleep(10)




send_msg_to_contact()
time.sleep(180)
driver.quit()