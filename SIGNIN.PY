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

def waitUntil(expectedCondition,optionalExpectedCondition=None):
    error1 = False
    error2 = False
    try:
        WebDriverWait(driver, 5,poll_frequency=1 ,  ignored_exceptions=[TimeoutException]).until(expectedCondition)
    except:
        error1 = True
    if (optionalExpectedCondition != None):
        try:
            WebDriverWait(driver, 3,poll_frequency=1 ,  ignored_exceptions=[TimeoutException]).until(optionalExpectedCondition)
        except Exception as E:
            error2 = True
    return (error1 or error2)

def SignIn(Driver):
    #opts = webdriver.ChromeOptions()
    #opts.add_argument("--disable-notifications")

    #websiteURL = "http://bort2an.com/"
    #serv_obj = Service("O:\DriveFiles\Drivers\chromedriver_win32 (1)\chromedriver.exe")

    #Driver = webdriver.Chrome(service=serv_obj,options=opts)
    #Driver.get(websiteURL)
    #Driver.maximize_window()


    #Driver.get('http://bort2an.com')
    Driver.get('https://dev--venerable-fenglisu-3497d9.netlify.app/login')

    #WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.ID, "loginBtn"))).click()

    #
    # #ClickFnID(Driver, "centerView", 1)
    # ClickFnHttp(Driver,"//*[@id='loginBtn']",1)
    # action = ActionChains(Driver)

    F = open('EmailTestCases.txt', 'r')
    Emails = [Email.rstrip('\n') for Email in F.readlines()] # Makes a list containing all email test cases
    F.close()

    F = open('PasswordTestCases.txt', 'r')
    Passwords = [Password.rstrip('\n') for Password in F.readlines()]  # Makes a list containing all Password test cases
    F.close()

    counter = 0  

    for Email in Emails:
        for Password in Passwords:
            counter += 1
            print("Test number: ", counter)
            print("Email: ", Email)
            print("Password: ", Password)
            print("")


            time.sleep(1)
            EmailField = SendKeysFnID(Driver, "login-email-input", Email, 1)  # Writes the email in the email field
            # time.sleep(1)
            PasswordField = SendKeysFnID(Driver, "login-password-input", Password, 1)  # Writes the password in the password field
            time.sleep(1)

            WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.ID,"login-submit-button"))).click()
            previousURL = Driver.current_url
            errorInChangingURL = waitUntil(EC.url_changes(previousURL))
            message = "Not Logged In"
            Assert(errorInChangingURL,False,message)
            # if mode == 1:
            #Driver.get('https://dev--venerable-fenglisu-3497d9.netlify.app/login')
            print("passed tests number: ", counter)