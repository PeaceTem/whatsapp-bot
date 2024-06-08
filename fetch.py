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

text = "The 2023 warnings from a renowned prophetess  warning about Tinubu's deception and desperation, begging her followers to free themselves from the political bondage of the APC. One year after, her prophesies are coming to pass and the people are in pain and anguish. May God hear the cry of His children and deliver us. amen                                                                                                     #Ekowa #OmoluabiEko #OurLagos                                                                                                 https://youtu.be/WOONBy6_dN0?si=TNpg_zyM2GugHrBd."


print("The work has started.")
# # Specify the user data directory where the Chrome profile with an active WhatsApp Web session is located
user_data_directory = r'C:\Users\USER\AppData\Local\Google\Chrome\User Data'

# # Initialize the Chrome webdriver with the existing WebDriver executable using the Service class
options = Options()
options.add_argument(f'--user-data-dir={user_data_directory}')
# # options.add_argument('--headless')
# # options.add_argument('--disable-gpu')
# # options.add_argument("remote-debugging-port=3333")
# # options.add_argument( "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.102 Safari/537.36")
# service = Service(executable_path=executable_path)
# driver = webdriver.Chrome(service=service, options=options)


driver = webdriver.Chrome(options=options)
driver.maximize_window()






driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
time.sleep(55)
print("Logged In")

contacts = []

def fetch_contacts():
    new_chat = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value="#app > div > div.two._aigs > div._aigv._aigw > header > div._ak0z > div > span > div:nth-child(5) > div > span > svg"))
    actions = ActionChains(driver)
    actions.click(new_chat)
    actions.perform()
    print("Found the New message box!")
    time.sleep(5)

    # contacts_box_path = "#app > div > div.two._aigs > div._aigu > div._aigv._aigw._aigx > span > div > span > div > div.x1n2onr6.x1n2onr6.xyw6214.x78zum5.x1r8uery.x1iyjqo2.xdt5ytf.x6ikm8r.x1odjw0f.x1hc1fzr.x1tkvqr7"
    # contacts_box = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=contacts_box_path))
    # contacts_box.send_keys(Keys.END)
    text_box_path = "#app > div > div.two._aigs > div._aigu > div._aigv._aigw._aigx > span > div > span > div > div.x1n2onr6.x1n2onr6.xyw6214.x78zum5.x1r8uery.x1iyjqo2.xdt5ytf.x6ikm8r.x1odjw0f.x1hc1fzr.x1tkvqr7 > div:nth-child(3) > div > div > div:nth-child(1) > div > div._ajzf._ajzg"
    text_box = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=text_box_path))
    print("About to scroll")
    ActionChains(driver).click(text_box).send_keys(Keys.END).perform()
    time.sleep(5)
    contact_names = driver.find_elements(by=By.CSS_SELECTOR, value="#app > div > div.two._aigs > div._aigu > div._aigv._aigw._aigx > span > div > span > div > div > div > div > div > div > div > div > div._ak8l > div._ak8o > div > div > span")
    time.sleep(5)
    print(contact_names)
    print("Has it worked?")

    for name in contact_names:
        print(name)
        print()
        contacts.append(name.title)

    df = pd.DataFrame(contacts, columns=["Name"])
    df.to_csv("new_contacts.csv", index=False)
    print("Saved to file")


fetch_contacts()
time.sleep(10)
driver.quit()