# Generated by Selenium IDE

from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import csv


  



def openInstance():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10) #seconds
    driver.get("https://myquiz.org/Lectures")
    driver.set_window_size(1115, 799)
    driver.find_element_by_id( "agreeUseCookiesAccept").click()
    print("Agreed to cookies")
    driver.find_element_by_id( "Email").send_keys("dave@excesss.com")
    driver.find_element_by_id( "Password").send_keys("xsXSC$STO2020!")
    driver.find_element(By.CSS_SELECTOR, ".SignProcess__FormBlock").click()
    driver.find_element(By.CSS_SELECTOR, ".SignProcess__Button").click()
    print("Clicked to sign in")
    return driver

def endInstance(driver):
  driver.quit()

def createQuiz(driver):
    try:
        driver.find_element_by_id( "Email").send_keys("dave@excesss.com")
        driver.find_element_by_id( "Password").send_keys("xsXSC$STO2020!")
        driver.find_element(By.CSS_SELECTOR, ".SignProcess__FormBlock").click()
        print("Clicked to sign in")

        driver.find_element(By.CSS_SELECTOR, ".SignProcess__Button").click()
        driver.find_element_by_id( "topQuizCreateBtn").click()
        print("Clicked to create quiz")

        driver.find_element_by_id( "Theme").click()
        driver.find_element_by_id( "Theme").send_keys("Zeno\'s pLEASE")
        print("Wrote title of game")

        driver.find_element(By.CSS_SELECTOR, ".menuItem:nth-child(2) .menuItem__icon").click()
        print("Clicked to WHEN")

        
    # select = Select(driver.find_element_by_id('StartTimeHour'))
    # select.select_by_value("8")
    # print("selected 8pm")
    ## driver.find_element_by_id( "StartTimeHour").click()
        ##dropdown = driver.find_element_by_id( "StartTimeHour")
        ##dropdown.find_element(By.XPATH, "//option[. = '8']").send_keys(Keys.ENTER)
        ##driver.find_element(By.CSS_SELECTOR, ".mobilehide .menuTab:nth-child(2) > .menuTab__icon").click()
        
        ##driver.find_element(By.CSS_SELECTOR, ".nextQuizButton").click()
        driver.find_element(By.CSS_SELECTOR, ".menuItem:nth-child(3) .menuItem__iconBlock").click()
        print("Clicked NEXT to get to Whom")
        
        driver.find_element(By.CSS_SELECTOR, ".menuItem:nth-child(4) .menuItem__iconBlock").click()
        ##driver.find_element(By.CSS_SELECTOR, ".nextQuizButton").click()
        print("Clicked NEXT to get to How")
        
    
        ##driver.find_element_by_id( "menuActions__nextButton").click()
        # driver.find_element(By.CSS_SELECTOR, ".newQuizEditor .menuTab:last-child").click()
        #print("Clicked NEXT to get to Question Menu?")
    
        
        #driver.find_element(By.CSS_SELECTOR, ".addQuestionModal__ButtonContainer:nth-child(6) .addQuestionModal__AddButtonDescription").click()
        #driver.find_element(By.CSS_SELECTOR, ".slideSelectorContainer__item:nth-child(1) > .slideSelectorContainer__itemText > img").click()
        driver.find_element(By.CSS_SELECTOR, ".questionEditor__title").click()
    except:
        print("Nope")
    finally:
        return driver

  

def  addAllQuestions(driver,myFile):
  myFile="weeks/"+myFile
  csv_file= open(myFile, encoding="utf-8-sig")
  csv_reader = csv.DictReader(csv_file)
  waitO = WebDriverWait(driver, 10 )
  for row in csv_reader:
    driver.find_element(By.NAME, "QuestionText").clear()
    driver.find_element(By.NAME, "QuestionText").send_keys(row["Question Text"])
    driver.find_element(By.NAME, "StepTitle").clear()
    driver.find_element(By.NAME, "StepTitle").send_keys(row["Step Title"])
    print("Created and filled",row["Step Title"])
    driver.find_element(By.CSS_SELECTOR, ".tooltipButton:nth-child(2)").click()


    # next, We scroll down
    """ scroll = driver.find_element(By.CLASS_NAME,'questionEditor__questionData')
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll) 
    manuallyAdvance=driver.find_element(By.NAME, "IsNotUseTimerSetting_checkbox")
    waitO.until(EC.element_to_be_clickable(manuallyAdvance))
    manuallyAdvance.click()
    driver.find_element(By.NAME, "StepTitle").click()
    driver.find_element(By.NAME, "StepTitle").send_keys(row["Step Title"])
    print("Created and filled",row["Step Title"])
    newQButton=driver.find_element(By.CSS_SELECTOR, ".addQuestionModal__ButtonContainer:nth-child(6) .addQuestionModal__AddButtonDescription")
    newQButton.click() 
    #driver.find_element(By.CSS_SELECTOR, ".addQuestionModal__ButtonContainer:nth-child(6) .addQuestionModal__AddButtonDescription").click()
    driver.find_element(By.CSS_SELECTOR, ".slideSelectorContainer__item:nth-child(1) > .slideSelectorContainer__itemText > img").click() """
        


  driver.find_element(By.NAME, "QuestionText").click()
  driver.find_element(By.NAME, "QuestionText").send_keys("That's all folks!")
  driver.find_element(By.CSS_SELECTOR, ".editorRow:nth-child(8) > .editorRow__cell").click()
  driver.find_element(By.NAME, "StepTitle").click()
  driver.find_element(By.NAME, "StepTitle").send_keys("The End")

  driver.find_element(By.CSS_SELECTOR, ".saveQuizButton").click()
  driver.find_element(By.CSS_SELECTOR, "#createQuizModal .modal__tableCell").click()

  csv_file.close()


