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

def withgoogle(Driver):
    Driver.get('http://bort2an.com') 
    currentHandle = Driver.current_window_handle
    gl=ClickFnID(Driver,"login-with-google",1)

    email="seif.albaghdady02@gmail.com"
    email = "powerwall.69@gmail.com"
    passwo="seifseifsei"
    passwo="powerwall69420"
    #gl2=SendKeysFnID(Driver,"identifierId",email,1)

    #Driver.maximize_window()
    #WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='identifierId']")))
    #ClickFnHttp(Driver,"//*[@id='identifierId']",1)
    #action = ActionChains(Driver)
    # switch_to()
    # Driver.switch_to()

    
    allhandles = Driver. window_handles
    print(allhandles)
    # input()
    # input()
    for handle in allhandles:
        if handle != currentHandle:
            Driver.switch_to.window(handle)
            break
    
    EmailField = SendKeysFnID(Driver, "identifierId", email, 1)

    WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='identifierNext']/div/button"))).click()

    PasswordField = SendKeysFnname(Driver, "password", passwo, 1)  # Writes the password in the password field
    
    time.sleep(1)

    WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id=;passwordNext']/div/button"))).click()


    