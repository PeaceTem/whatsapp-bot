import time
import webbrowser as web
from datetime import datetime
from typing import Optional
from urllib.parse import quote

import pyautogui as pg

from pywhatkit.core import core, exceptions, log

pg.FAILSAFE = False

core.check_connection()
import timeit


time.sleep(0.5)

def send(contacts: list, message: str) -> None:

    
    web.open(f"https://web.whatsapp.com")
    time.sleep(30)

    # add manual delay after 10 messages: 5 sec
    for contact in contacts:
        pg.hotkey('ctrl', 'alt', '/')
        time.sleep(1)
        # print("The keys have been pressed!")
        pg.write(contact)
        time.sleep(2)
        # print("The text has been searched!")
        pg.press("enter")
        # print("Just opened the user chats")
        time.sleep(1)
        pg.write(message)
        # print("The text has been entered!")
        time.sleep(1)
        pg.press("enter")
        time.sleep(1)
        # print("The message has just been sent!")

contacts = [
    # "Jumoke",
    "Ayomide Octave", 
    # "Habyaad Critical Thinker",
    # "Dildara Goodness 2",
    # "The Most Concept - Qudus",
    # "Tosin UI WinRaR",
    "~GlassOfCode 🍷",
    # "Victor Iroko UI",
    # "+234 809 359 3598",
    # "Octave Analytics",
    # "Taye Church 2",
    # "Elizabeth",
    # "Bro. Seun WhatsApp",
    # "Marvelous",
    # "Kehinde Pablos",
    # "#mercytorchservices",
    # "Owolabi Christianah",
    # "Bunmi Binuyo 2",
    # "Bakare Precious UI",
    # "Oladisea WinRAR",
    # "Thunder God Bolu Goodness",
    # # "Ajani Ezekiel Juvenile",
    # "Lanre UI",
    # "Emmanuel Adegboye",
    # "Yinbol",
    # "David",
    # "Deolu UI",
    # "Mr Vang",
    # "Peter🙇 Ojo",
    # "G Fresh",
    # "Cixcode"
    ]
message = r"""The 2023 warnings from a renowned prophetess  warning about Tinubu's deception and desperation, begging her followers to free themselves from the political bondage of the APC. One year after, her prophesies are coming to pass and the people are in pain and anguish. May God hear the cry of His children and deliver us. amen                                                            #Ekowa #OmoluabiEko #OurLagos                                                                         https://youtu.be/WOONBy6_dN0?si=TNpg_zyM2GugHrBd"""
send(contacts, message)
