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
    driver.get("https://www.instagram.com/accounts/login")
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
    images_unique=[]
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
        # Retrive the html
        html_to_parse=str(driver.page_source)
        html=bs(html_to_parse,"html5lib")
        # Get the image's url
        images_url=html.findAll("img", {"class": "FFVAD"})

        # Check if they are unique
        in_first = set(images_unique)
        in_second = set(images_url)

        in_second_but_not_in_first = in_second - in_first

        result = images_unique + list(in_second_but_not_in_first)
        images_unique=result
    # Close the webdriver     
    driver.close()


    
    for i in range(len(z)):
        name="image"+str(i)+".jpg"
        # Save each image.jpg file
        with open(name, 'wb') as handler:
            
            img_data = requests.get(z[i].get("src")).content
            handler.write(img_data)
    return



