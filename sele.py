from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import time
driver = webdriver.Chrome()
# By = webdriver.common.by.By()

    # web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
// https://web.whatsapp.com/send?phone=+256762732760&text=This is an automated message sent using selenium in python
class WhatsApp:

    @classmethod
    def open_browser(cls, phone_no, message, *args, **kwargs):
        driver.get(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
        title = driver.title
        url = driver.current_url
        print(title)
        print(url)
        time.sleep(30)

    


# driver.get("https://web.whatsapp.com/")
# driver.implicitly_wait(60)

# driver.current_window_handle

# driver.implicitly_wait(50)

# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()
# driver.implicitly_wait(5)

# message = driver.find_element(by=By.ID, value="message")
# text = message.text
# print(text)

WhatsApp.open_browser("+2349164702871", "This is an automated message sent using selenium in python.")

driver.quit()

