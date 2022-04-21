# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCreateQuiz():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createQuiz(self):
    self.driver.find_element(By.ID, "burger").click()
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.ID, "Email").send_keys("dave@excesss.com")
    self.driver.find_element(By.ID, "Password").send_keys("xsXSC$STO2020!")
    self.driver.find_element(By.CSS_SELECTOR, ".SignProcess__FormBlock").click()
    self.driver.find_element(By.CSS_SELECTOR, ".SignProcess__Button").click()
    self.driver.find_element(By.ID, "topQuizCreateBtn").click()
    self.driver.get("https://myquiz.org/Lectures")
    self.driver.set_window_size(1115, 799)
    self.driver.find_element(By.ID, "topQuizCreateBtn").click()
    self.driver.find_element(By.ID, "Theme").click()
    self.driver.find_element(By.ID, "Theme").send_keys("Zeno\'s Read Along 1/6 TEST")
    self.driver.find_element(By.CSS_SELECTOR, ".menuItem:nth-child(2) .menuItem__Title").click()
    self.driver.find_element(By.ID, "StartTimeHour").click()
    dropdown = self.driver.find_element(By.ID, "StartTimeHour")
    dropdown.find_element(By.XPATH, "//option[. = '8']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mobilehide .menuTab:nth-child(2) > .menuTab__Title").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nextQuizButton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nextQuizButton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nextQuizButton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addQuestionModal__ButtonContainer:nth-child(6) .addQuestionModal__AddButtonDescription").click()
    self.driver.find_element(By.CSS_SELECTOR, ".slideSelectorContainer__item:nth-child(1) > .slideSelectorContainer__itemText > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".questionEditor__title").click()
    self.driver.find_element(By.NAME, "QuestionText").click()
    self.driver.find_element(By.NAME, "QuestionText").send_keys("This is question Number 1")
    self.driver.find_element(By.CSS_SELECTOR, ".editorField:nth-child(6) .checkbox__label").click()
    self.driver.find_element(By.NAME, "StepTitle").click()
    self.driver.find_element(By.NAME, "StepTitle").send_keys("R1Q1")
    self.driver.find_element(By.CSS_SELECTOR, ".tooltipButton:nth-child(2)").click()
    self.driver.find_element(By.NAME, "QuestionText").click()
    self.driver.find_element(By.NAME, "QuestionText").send_keys("This is question Number 2")
    self.driver.find_element(By.NAME, "StepTitle").click()
    self.driver.find_element(By.NAME, "StepTitle").send_keys("R1Q2")
    self.driver.find_element(By.CSS_SELECTOR, ".tooltipButton:nth-child(2)").click()
    self.driver.find_element(By.NAME, "QuestionText").click()
    self.driver.find_element(By.NAME, "QuestionText").send_keys("This is question Number 3")
    self.driver.find_element(By.CSS_SELECTOR, ".editorRow:nth-child(8) > .editorRow__cell").click()
    self.driver.find_element(By.NAME, "StepTitle").click()
    self.driver.find_element(By.NAME, "StepTitle").send_keys("R1Q3")
    self.driver.find_element(By.CSS_SELECTOR, ".saveQuizButton").click()
    self.driver.find_element(By.CSS_SELECTOR, "#createQuizModal .modal__tableCell").click()
  
