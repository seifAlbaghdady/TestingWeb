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

def Forget(Driver):
    #opts = webdriver.ChromeOptions()
    #opts.add_argument("--disable-notifications")

    #websiteURL = "http://bort2an.com/"
    #serv_obj = Service("O:\DriveFiles\Drivers\chromedriver_win32 (1)\chromedriver.exe")

    #Driver = webdriver.Chrome(service=serv_obj,options=opts)
    #Driver.get(websiteURL)
    #Driver.maximize_window()


    Driver.get('http://bort2an.com') 

    myemail="seif.albaghdady02@gmail.com"
    wrongpass="seiflol12121212"

    EmailField = SendKeysFnID(Driver, "login-email-input", myemail, 1)  # Writes the email in the email field
    # time.sleep(1)
    PasswordField = SendKeysFnID(Driver, "login-password-input", wrongpass, 1)  # Writes the password in the password field
    time.sleep(1)

    WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.ID,"login-submit-button"))).click()

    time.sleep(3)
    WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='login-column-left']/div/div[5]/button"))).click()
    
    
    time.sleep(10)