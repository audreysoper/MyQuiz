# Generated by Selenium IDE

from multiprocessing.connection import wait
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import csv


   



class TestCreateQuiz():
  def setup_method(self):
    
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def createQuiz(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10) #seconds
    with open('zenos1-13test.csv') as csv_file:
      csv_reader = csv.DictReader(csv_file)

    self.driver.get("https://myquiz.org/Lectures")
    self.driver.set_window_size(1115, 799)
    self.driver.find_element(By.ID, "agreeUseCookiesAccept").click()
    print("Agreed to cookies")

    self.driver.find_element(By.ID, "Email").send_keys("dave@excesss.com")
    self.driver.find_element(By.ID, "Password").send_keys("xsXSC$STO2020!")
    self.driver.find_element(By.CSS_SELECTOR, ".SignProcess__FormBlock").click()
    self.driver.find_element(By.CSS_SELECTOR, ".SignProcess__Button").click()
    print("Clicked to sign in")

    self.driver.find_element(By.CSS_SELECTOR, ".SignProcess__Button").click()
    self.driver.find_element(By.ID, "topQuizCreateBtn").click()
    print("Clicked to create quiz")

    self.driver.find_element(By.ID, "Theme").click()
    self.driver.find_element(By.ID, "Theme").send_keys("Zeno\'s pLEASE")
    print("Wrote title of game")

    self.driver.find_element(By.CSS_SELECTOR, ".menuItem:nth-child(2) .menuItem__icon").click()
    print("Clicked to WHEN")

    
   # select = Select(self.driver.find_element_by_id('StartTimeHour'))
   # select.select_by_value("8")
   # print("selected 8pm")
   ## self.driver.find_element(By.ID, "StartTimeHour").click()
    ##dropdown = self.driver.find_element(By.ID, "StartTimeHour")
    ##dropdown.find_element(By.XPATH, "//option[. = '8']").send_keys(Keys.ENTER)
    ##self.driver.find_element(By.CSS_SELECTOR, ".mobilehide .menuTab:nth-child(2) > .menuTab__icon").click()
    
    ##self.driver.find_element(By.CSS_SELECTOR, ".nextQuizButton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".menuItem:nth-child(3) .menuItem__iconBlock").click()
    print("Clicked NEXT to get to Whom")
    
    self.driver.find_element(By.CSS_SELECTOR, ".menuItem:nth-child(4) .menuItem__iconBlock").click()
    ##self.driver.find_element(By.CSS_SELECTOR, ".nextQuizButton").click()
    print("Clicked NEXT to get to How")
    
   
    ##self.driver.find_element(By.ID, "menuActions__nextButton").click()
     # self.driver.find_element(By.CSS_SELECTOR, ".newQuizEditor .menuTab:last-child").click()
      #print("Clicked NEXT to get to Question Menu?")
  
    
    #self.driver.find_element(By.CSS_SELECTOR, ".addQuestionModal__ButtonContainer:nth-child(6) .addQuestionModal__AddButtonDescription").click()
    #self.driver.find_element(By.CSS_SELECTOR, ".slideSelectorContainer__item:nth-child(1) > .slideSelectorContainer__itemText > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".questionEditor__title").click()

    for row in csv_reader:
      self.driver.find_element(By.NAME, "QuestionText").click()
      self.driver.find_element(By.NAME, "QuestionText").send_keys(row["Question Text"])
      self.driver.find_element(By.CSS_SELECTOR, ".editorField:nth-child(6) .checkbox__label").click()
      self.driver.find_element(By.NAME, "StepTitle").click()
      self.driver.find_element(By.NAME, "StepTitle").send_keys(row["Step Title"])
      print("Created and filled",row["Step Title"])
      self.driver.find_element(By.CSS_SELECTOR, ".tooltipButton:nth-child(2)").click()  # Copy Question Button


    self.driver.find_element(By.NAME, "QuestionText").click()
    self.driver.find_element(By.NAME, "QuestionText").send_keys("That's all folks!")
    self.driver.find_element(By.CSS_SELECTOR, ".editorRow:nth-child(8) > .editorRow__cell").click()
    self.driver.find_element(By.NAME, "StepTitle").click()
    self.driver.find_element(By.NAME, "StepTitle").send_keys("The End")

    self.driver.find_element(By.CSS_SELECTOR, ".saveQuizButton").click()
    self.driver.find_element(By.CSS_SELECTOR, "#createQuizModal .modal__tableCell").click()
  
bop= TestCreateQuiz()
bop.setup_method()
bop.createQuiz()
bop.teardown_method()