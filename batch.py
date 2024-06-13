import threading
import time
from selenium import webdriver

driver2 = webdriver.Edge()
driver2.maximize_window()

def task1():
    while True:
        print("Task 1 is running")
        time.sleep(1)

def task2():
    while True:
        print("Task 2 is running")
        time.sleep(1)

def task3():
    while True:
        print("Task 3 is running")
        time.sleep(1)

def task4():
    while True:
        print("Task 4 is running")
        time.sleep(1)

if __name__ == "__main__":
    # Create threads
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)
    thread3 = threading.Thread(target=task3)
    thread4 = threading.Thread(target=task4)

    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Keep the main thread running, otherwise the program will exit
    while True:
        time.sleep(1)

driver.quit()