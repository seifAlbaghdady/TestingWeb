import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (TimeoutException,NoSuchElementException,ElementNotVisibleException)
from selenium.webdriver.support.ui import Select

from utilities import *

def reserve(Driver):
    currentHandle = Driver.current_window_handle
    allhandles = Driver.window_handles
    print(allhandles)
    # input()
    # input()
    for handle in allhandles:
        if handle != currentHandle:
            Driver.switch_to.window(handle)
            break

    #event1 = ClickFnHttp(Driver, "//*[@id='eventsByLocationSection']/div/div[1]/div/a/img", 1)
    #event = ClickFnHttp(Driver, "//*[@id='eventsByLocationSection']/div/div[1]/div/a", 1)
    time.sleep(5)
    Driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@data-testid='event-card']")))
    Events = Driver.find_elements(By.XPATH,"//*[@data-testid='event-card-image']")
    chooseEvent = Events[0]
    # title = Driver.find_element(By.CLASS_NAME,"tile-name")
    # Driver.execute_script("arguments[0].scrollIntoView();",chooseEvent)
    ActionChains(Driver).move_to_element(chooseEvent).click(chooseEvent).perform()

    
    ClickFnID(Driver, "event-card-image", 1)

    #WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='eventsByLocationSection']/div/div[1]/div/a/img"))).click()
    time.sleep(5)
    #re =ClickFnHttp(Driver, "//*[@id='centerView']/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/button", 1)
    Driver.execute_script("window.scrollTo(0, 1000);")
    WebDriverWait(Driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='centerView']/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/button"))).click()
    

    WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='staticModal']/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/button[2]"))).click()

    
    WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='staticModal']/div/div/div/div[1]/div[3]/button"))).click()

    fn="seif"
    sn="albaghdady"
    email="seif.albaghdady02@gmail.com"

    firstanmeee= SendKeysFnID(Driver, "login-email-input", fn, 1)
    secondname=SendKeysFnname(Driver, "lastname", sn, 1)
    emailll=SendKeysFnname(Driver, "email", email, 1)
    
    
    firstanmeee= SendKeysFnHttp(Driver, "/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/form/div/div/div/div[3]/div[1]/div[1]/input", fn, 1)
    
    secondname=SendKeysFnHttp(Driver, "/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/form/div/div/div/div[3]/div[1]/div[2]/input", sn, 1)
    
    emailll=SendKeysFnHttp(Driver, "/html/body/div/main/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/form/div/div/div/div[3]/div[2]/input", email, 1)

    
    WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='staticModal']/div/div/div/div[1]/div[3]/button[1]"))).click()