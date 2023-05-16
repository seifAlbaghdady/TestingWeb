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

from SIGNIN import SignIn
from SignUp import SignUp
from createEventUpdated import createEvent
from fav import fav
from SignInWithGoogle import withgoogle
from Reserve import reserve

from forgetpass import Forget

opts = webdriver.ChromeOptions()
opts.add_argument("--disable-notifications")

websiteURL = "https://dev--venerable-fenglisu-3497d9.netlify.app/"
serv_obj = Service("O:\DriveFiles\Drivers\chromedriver_win32 (1)\chromedriver.exe")

Driver = webdriver.Chrome(service=serv_obj,options=opts)
Driver.get(websiteURL)
Driver.maximize_window()


Driver.get('https://dev--venerable-fenglisu-3497d9.netlify.app/') 

#Forget(Driver)

SignIn(Driver)
createEvent(Driver)
# try:
#reserve(Driver)
#fav(Driver)
# except Exception as E:
#     print(E)

input()#fav(Driver)
#withgoogle(Driver)
#time.sleep(30)
#createEvent(Driver)
#SignUp(Driver)
#time.sleep(30)