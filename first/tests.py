import pandas as pd
import numpy as np
from selenium import webdriver
from whats import the_the, send_bulk_msg
import time


print("The Automation is about to start!")
df = pd.read_csv("new_contacts.csv")

df.drop_duplicates()
df = df.head(1000)
print(df)
# Split the DataFrame into 4 parts
dfs = np.array_split(df, 4)
tehj = the_the()

def test_one():
    new_package = dfs[0]["Name"]
    
    driver1 = webdriver.Edge()
    driver1.maximize_window()

    
    driver1.get("https://web.whatsapp.com")
    print("Scan QR Code for Driver 1, And then Enter")
    time.sleep(500)
    print("Logged In")
    
    send_bulk_msg(driver1, new_package.tolist())
    time.sleep(99999)
    driver1.quit()
    assert True

def test_two():
    time.sleep(10)
    new_package2 = dfs[1]["Name"]
    
    driver2 = webdriver.Chrome()
    driver2.maximize_window()

    driver2.get("https://web.whatsapp.com")
    print("Scan QR Code for Driver 2, And then Enter")
    time.sleep(500)
    print("Logged In")
    send_bulk_msg(driver2, new_package2.tolist())
    time.sleep(99999)
    driver1.quit()

    assert True



def test_three():
    time.sleep(20)

    new_package_3 = dfs[2]["Name"]
    
    driver3 = webdriver.Edge()
    driver3.maximize_window()

    
    driver3.get("https://web.whatsapp.com")
    print("Scan QR Code for Driver 1, And then Enter")
    time.sleep(500)
    print("Logged In")

    send_bulk_msg(driver3, new_package_3.tolist())
    time.sleep(99999)
    driver1.quit()

    assert True

def test_four():
    time.sleep(30)
    new_package_3 = dfs[3]["Name"]
    
    driver4 = webdriver.Chrome()
    driver4.maximize_window()

    driver4.get("https://web.whatsapp.com")
    print("Scan QR Code for Driver 2, And then Enter")
    time.sleep(500)
    print("Logged In")
    send_bulk_msg(driver4, new_package_3.tolist())
    time.sleep(99999)
    driver1.quit()

    assert True


# pytest -n 3 --capture=no test_example.py
# New-NetFirewallRule -DisplayName "Block IP" -Direction Inbound -RemoteAddress  216.58.223.206 -Action Block

