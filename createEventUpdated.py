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

def createEvent(Driver):
    #opts = webDriver.ChromeOptions()
    #opts.add_argument("--disable-notifications")

    #websiteURL = "http://bort2an.com/"
    #serv_obj = Service("O:\DriveFiles\Drivers\chromeDriver_win32 (1)\chromeDriver.exe")

    #Driver = webDriver.Chrome(service=serv_obj,options=opts)
    #Driver.get(websiteURL)
    #Driver.maximize_window()

    # time.sleep(5)
    WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='centerView']/div[1]/div[2]/a[1]/div")))
    #ClickFnID(Driver, "centerView", 1)
    ClickFnHttp(Driver,"//*[@id='centerView']/div[1]/div[2]/a[1]/div",1)
    action = ActionChains(Driver)

    WebDriverWait(Driver, 10).until(EC.presence_of_element_located((By.NAME, "eventtitle")))
    #eventtitle
    try:
        title = "Killing  koalas"
        button = Driver.find_element(By.NAME, "eventtitle")
        button.send_keys(title)
        # ClickFnHttp(Driver,"//*[@id='react-aria2976914829-3-tabpane-first']/div/div/div[1]/div[1]/div[2]/div/div[2]/input",1)
        # SendKeysFnHttp(Driver,"//*[@id='react-aria2976914829-3-tabpane-first']/div/div/div[1]/div[1]/div[2]/div/div[2]/input",Eventt,1)

        # SendKeysFnname(Driver,"organizer",Seif,1)
        
        # ClickFnName(Driver,"organizer",1)

        organizerName = "Seif B."
        button = Driver.find_element(By.NAME, "organizer")
        button.send_keys(organizerName)

        #############################################
        eventCategory = Driver.find_element(By.ID,"eventType")
        select = Select(Driver.find_element(By.ID,"eventType"))
        select.select_by_visible_text('Attraction')
        #############################################
        eventSubCategory = Driver.find_element(By.ID,"eventSubTopic")
        select = Select(Driver.find_element(By.ID,"eventSubTopic"))
        select.select_by_visible_text('Music')
        #####################################################
        addTag = Driver.find_element(By.XPATH,"//button[(text() = 'Add')]")
        tagsNeeded = ["music","rock","Science","drama","schoolholidays","scrum","drawing","poetry","popup","politics"]
        tags = Driver.find_element(By.NAME,"tags")
        # action.scroll_to_element(addTag).perform()
        for tag in tagsNeeded:
            tags.send_keys(tag)
            addTag.click()
            print(tag)

        Driver.execute_script("arguments[0].scrollIntoView();",addTag)

        Driver.find_element(By.NAME,"venuesearch")

        # onlineEvents = Driver.find_element(By.NAME,"venueType")
        # onlineEvents = Driver.find_element(By.XPATH,"//label[contains(text(),'Online')]")

        # Driver.execute_script("arguments[0].scrollIntoView();",onlineEvents)
        # onlineEvents.click()
        
        WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='centerView']/div[1]/div[1]/div[2]/div[3]/div[2]/a"))).click()

        # save = driver.find_element(By.XPATH,"//*[@id='react-aria9053612422-1-tabpane-second']/div[2]/button")
        # save.click()


        # imagePort = driver.find_element(By.XPATH,"//*[@id='upload__btn']")
        # imagePort.send_keys("oh.jpg")

        
        # tryaddsumm=SendKeysFnID(Driver,"outlined-error","so ya soo habiby habso",1)

        # tryaddsumm2=SelectFnHttp(Driver,"//*[@id='outlined-error']","so ya soo habiby habso",1)

        

        WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='centerView']/div[1]/div[1]/div[2]/div[3]/div[4]/a"))).click()

        WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pub_button']"))).click()
        WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pub_button']"))).click()
        WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pub_button']"))).click()
        WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pub_button']"))).click()
        WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pub_button']"))).click()
        WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pub_button']"))).click()
        WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pub_button']"))).click()

    except: 
        pass
    input()
