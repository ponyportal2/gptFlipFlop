from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from watchdog.events import FileSystemEventHandler

import pickle
import time

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
from watchdog.observers import Observer

kGlobalBotNum = 1
kMessageDelayMultiplier = 0.2


def webDriverInit():
    d = DesiredCapabilities.CHROME
    d['goog:loggingPrefs'] = {'browser': 'ALL'}
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')
    driverFile = '*googlechrome /Users/sharkmer/chrome.sh'
    inputDriver = webdriver.Chrome(
        driverFile, chrome_options=chrome_options, desired_capabilities=d)
    return inputDriver


def loadPoe(inputDriver):
    URL = 'https://poe.com'
    inputDriver.get(URL)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        inputDriver.add_cookie(cookie)
    inputDriver.get(URL)


def fillMessage(message, driver):
    driver.execute_script(
        "document.querySelector('div.ChatMessageInputView_growWrap__mX_pX textarea').value = " + message)


def sendMessage(driver):
    element = driver.find_element(By.CSS_SELECTOR,
                                  '.ChatMessageInputView_sendButton__reEpT')
    element.click()


def getLast(driver):
    element = driver.find_element(By.CSS_SELECTOR,
                                  '.ChatMessagesView_messageExpander__MmKBH .ChatMessage_messageWrapper__Zf87D')
    return element.text
