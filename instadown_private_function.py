import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time
import pyautogui as pg
from random import random
def download(url,userlogin,passlogin):
    profile=str(url)
    user=str(username)
    password=str(passlogin)
    driver = webdriver.Firefox()
    driver.get()
    time.sleep(2)
    pg.press("tab",3,round(random(),2))
    time.sleep(round(random(),2))
    pg.typewrite(user,round(random(),2))
    pg.press("tab")
    time.sleep(round(random(),2))
    pg.typewrite(password,round(random(),2))
    time.sleep(round(random(),2))
    pg.press("enter")
    time.sleep(2)

    driver.get(profile)

    time.sleep(3)
    SCROLL_PAUSE_TIME = 1
    z=[]
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
            break
        last_height = new_height
        time.sleep(1)
        y=str(driver.page_source)
        html=bs(y,"html5lib")
        x=html.findAll("img", {"class": "FFVAD"})
        in_first = set(z)
        in_second = set(x)

        in_second_but_not_in_first = in_second - in_first

        result = z + list(in_second_but_not_in_first)
        z=result
    driver.close()


    nome="image"
    for i in range(len(z)):
        nome="image"+str(i)+".jpg"
        with open(nome, 'wb') as handler:
            #print(x[1].get("src"))
            img_data = requests.get(z[i].get("src")).content
            handler.write(img_data)
    return



