import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def Assert(parameter,value,message):

    try:
        assert parameter == value
    except AssertionError:
        print(message)

def ClickFnHttp(Driver,http,DelayTime = 1): #should pass http as string parameter
    try:
        button = Driver.find_element(by=By.XPATH,value=http)
        time.sleep(DelayTime)
        button.click()
        time.sleep(DelayTime)
    except Exception as E:
        print(E)

def ClickFnID(Driver,ID,DelayTime = 1): #pass ID of button
    try:
        button = Driver.find_element(by=By.ID, value=ID)
        time.sleep(DelayTime)
        button.click()
        time.sleep(DelayTime)
    except:
        print("Element not found.")


def ClickFnName(Driver,ID,DelayTime = 1): #pass ID of button
    try:
        button = Driver.find_element(by=By.NAME, value=ID)
        time.sleep(DelayTime)
        button.click()
        time.sleep(DelayTime)
    except Exception as E:
        print(E)


def SendKeysFnHttp(Driver,http,value,DelayTime = 1):
    try:
        button = Driver.find_element(by=By.XPATH, value=http)
        time.sleep(DelayTime)
        button.send_keys(value)
        time.sleep(DelayTime)
    except Exception as E:
        print(E)

def SendKeysFnname(Driver,name,value,DelayTime = 1):
    try:
        button = Driver.find_element(by=By.NAME, value=name)
        time.sleep(DelayTime)
        button.send_keys(value)
        time.sleep(DelayTime)
    except Exception as E:
        print(E)



def SendKeysFnID(Driver,ID,value,DelayTime = 1):
    try:
        button = Driver.find_element(by=By.ID, value=ID)
        time.sleep(DelayTime)
        button.send_keys(value)
        time.sleep(DelayTime)
    except:
        print("Element not found.")

def SelectFnHttp(Driver,http,index,DelayTime = 1):
    try:
        Field = Select(Driver.find_element(by=By.XPATH, value=http))
        time.sleep(DelayTime)
        Field.select_by_index(index)
        time.sleep(DelayTime)
    except:
        print("Element not found.")

def SelectFnHttp(Driver,ID,index,DelayTime = 1):
    try:
        Field = Select(Driver.find_element(by=By.ID, value=ID))
        time.sleep(DelayTime)
        Field.select_by_index(index)
        time.sleep(DelayTime)
    except:
        print("Element not found.")