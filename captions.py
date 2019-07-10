# do not modify below
from time import sleep
import csv
import random
import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

waittime = 10							# seconds browser waits before giving up
sleeptime = [5, 15]						# random seconds range before loading next video id


def getTranscript(video_id, driver):
    """Return the trancripts in a Array structure.
        Expect : ['00:00','something here'...]
    """
    # sleep(random.uniform(sleeptime[0], sleeptime[1]))

    # navigate to video
    driver.get("https://www.youtube.com/watch?v=" + video_id)
    sleep(3)
    try:
        options = driver.find_elements_by_css_selector("yt-icon-button.dropdown-trigger > button:nth-child(1)")
    except:
        msg = 'could not find options button'
        return msg
    
    try:
        options[2].click()
    except:
        msg = 'could not click options button'
        return msg

    try:
        element = WebDriverWait(driver, waittime).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#items > ytd-menu-service-item-renderer:nth-child(2) > paper-item")))
    except:
        msg = 'could not find transcript in options menu'
        return msg

    try:
        element.click()
    except:
        msg = 'could not click'
        return msg

    try:
        element = WebDriverWait(driver, waittime).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-transcript-body-renderer.style-scope")))
    except:
        msg = 'could not find transcript text'
        return msg

    captions_arr = element.text.splitlines()

    return captions_arr

def getTimestamps(captions_arr,client):
    """Return the time stamps looking for the clien in it.
        Expect: ['00:00,some text CLIENT continue'...]
    """
    timestamps = []
    pre = ""
    for e in captions_arr:
        if(client in e):
            timestamps.append("{time},{text}".format(time=pre,text=e))
        pre = e
    return timestamps
