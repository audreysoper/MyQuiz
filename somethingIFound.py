csv_file= open('zenos1-13test.csv')
csv_reader = csv.DictReader(csv_file)
waitO = WebDriverWait(driver, 10 )
for row in csv_reader:
  driver.find_element(By.NAME, "QuestionText").click()
  driver.find_element(By.NAME, "QuestionText").send_keys(row["Question Text"])
  driver.find_element(By.NAME, "StepTitle").click()
  driver.find_element(By.NAME, "StepTitle").send_keys(row["Step Title"])
  print("Created and filled",row["Step Title"])
  copyButton=driver.find_element(By.CSS_SELECTOR, ".tooltipButton:nth-child(2)")
  ActionChains(driver).move_to_element(copyButton).perform()
  waitO.until(EC.element_to_be_clickable(copyButton)); 
  copyButton.click() 


scroll = driver.find_element(By.CLASS_NAME,'questionEditor__questionData')
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)