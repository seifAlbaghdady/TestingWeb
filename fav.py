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

def fav(Driver):

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
    Driver.execute_script("window.scrollTo(0, 500);")
###########
    #close = ClickFnHttp(Driver, "//*[@id='staticModal']/div/div/div/button/svg", 1)
    # WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='staticModal']/div/div/div/button")))
    # ClickFnHttp(Driver,"//*[@id='staticModal']/div/div/div/button",1)
    # action = ActionChains(Driver)


    # WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='centerView']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[2]/button")))
    # ClickFnHttp(Driver,"//*[@id='centerView']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[2]/button",1)
    # action = ActionChains(Driver)
    
    #favv= ClickFnHttp(Driver, "//*[@id='centerView']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[2]/button/svg/path", 1)
    
    # WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='centerView']/div[2]/div[2]/div/div[2]/div[1]/button[2]")))
    # ClickFnHttp(Driver,"//*[@id='centerView']/div[2]/div[2]/div/div[2]/div[1]/button[2]",1)
    # action = ActionChains(Driver)

    # WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='centerView']/div[1]/div[2]/a[2]/div")))
    # ClickFnHttp(Driver,"//*[@id='centerView']/div[1]/div[2]/a[2]/div",1)
    # action = ActionChains(Driver)
    
    time.sleep(3)
    
    WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.ID, "645a568db72d59a07bacfa52"))).click()

    time.sleep(3)
    Driver.execute_script("window.scrollTo(1000, 0);")
    # Driver.execute_script("window.scrollTo(1000, 0);")
    
    # WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='centerView']/div[1]/div[2]/div/button"))).click()
    WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='centerView']/div[1]/div[2]/div/button")))
    #ClickFnID(Driver, "centerView", 1)
    ClickFnHttp(Driver,"//*[@id='centerView']/div[1]/div[2]/div/button",1)
    action = ActionChains(Driver)

    
    WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='centerView']/div[1]/div[2]/div/div/a[3]")))
    #ClickFnID(Driver, "centerView", 1)
    ClickFnHttp(Driver,"//*[@id='centerView']/div[1]/div[2]/div/div/a[3]",1)
    # ClickFnHttp(Driver,"//*[@id='centerView']/div[1]/div[2]/div/button",1)
    # action = ActionChains(Driver)
    time.sleep(3)
    Driver.execute_script("window.scrollTo(0, 1000);")
    Driver.execute_script("window.scrollTo(0, 1000);")
    Driver.execute_script("window.scrollTo(0, 1000);")
    


    time.sleep(3)
    Driver.execute_script("window.scrollTo(0, 1000);")
