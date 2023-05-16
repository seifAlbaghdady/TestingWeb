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

def SignUp(Driver):
#opts = webdriver.ChromeOptions()
#opts.add_argument("--disable-notifications")

#websiteURL = "http://bort2an.com/"
#serv_obj = Service("O:\DriveFiles\Drivers\chromedriver_win32 (1)\chromedriver.exe")

#Driver = webdriver.Chrome(service=serv_obj,options=opts)
#Driver.get(websiteURL)
#Driver.maximize_window()

    Driver.get("https://dev--venerable-fenglisu-3497d9.netlify.app/signup")

    F = open('EmailTestCases.txt', 'r')
    Emails = [Email.rstrip('\n') for Email in F.readlines()] # Makes a list containing all email test cases
    F.close()
    F = open('EmailTestCases2.txt', 'r')
    Emails2 = [Email.rstrip('\n') for Email in F.readlines()] # Makes a list containing all email test cases
    F.close()
    F = open('PASS.txt', 'r')
    Passwords = [Email.rstrip('\n') for Email in F.readlines()] # Makes a list containing all email test cases
    F.close()

    Email=Emails2[0]
    Email2=Emails2[0]
    Password=Passwords[0]
    fName="seif"
    lName="albaghdady"
    time.sleep(1)

    EmailField = SendKeysFnID(Driver, "email-input", Email, 1)  # Writes the email in the email field

    WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.ID,"submit-button"))).click()
    click1 = SendKeysFnID(Driver, "submit-button", 1)

    emailConfirm= SendKeysFnID(Driver, "emailConfirm", Email2, 1)

    expectedMessage = "Email address doesn't match. Please try again"


    firstname=SendKeysFnID(Driver, "firstName-input", fName, 1)

    lastname=SendKeysFnID(Driver, "lastName-input", lName, 1)
    PasswordField = SendKeysFnID(Driver, "password-input", Password, 1)  # Writes the password in the password field
    time.sleep(1)
    WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.ID,"submit-button"))).click()

    time.sleep(5)

    WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.ID,"SignupVerifyModal-AcceptButton"))).click()

    
    WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='SignupVerifyModal-AcceptButton']"))).click()

    time.sleep(5)