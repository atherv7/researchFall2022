import re
import os
import time
import random
import pandas as pd
from datetime import datetime
import shutil
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

c_path = 'chromedriver.exe'

def get_web_driver():  
    driver = webdriver.Chrome(executable_path=c_path)

    return driver

def wait(ob): 
    ob.implicitly_wait(60)

url = 'https://lib.guides.umd.edu/az.php?q=EconLit'
driver = get_web_driver() 
wait(driver)
driver.get(url)
wait(driver)
driver.find_element(By.CLASS_NAME, 's-lg-az-result-title').click() 