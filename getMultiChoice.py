# Generated by Selenium IDE

from lib2to3.pgen2 import driver
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import csv
import re
import urllib.request
import os
from concurrent.futures.thread import ThreadPoolExecutor
import concurrent.futures as futrs

  

def setup():
    msg=[]
    driver = webdriver.Firefox()
    driver.implicitly_wait(10) #seconds
    driver.get("https://myquiz.org/Lectures")
    driver.set_window_size(1115, 799)
    driver.find_element(By.ID, "cookiescript_accept").click()
    msg.append("Agreed to cookies")
    driver.find_element(By.ID, "Email").send_keys("dave@excesss.com")
    driver.find_element(By.ID, "Password").send_keys("xsXSC$STO2020!")
    driver.find_element(By.CSS_SELECTOR, ".SignProcess__FormBlock").click()
    driver.find_element(By.CSS_SELECTOR, ".SignProcess__Button").click()
    msg.append("Clicked to sign in")
    driver.implicitly_wait(2)
    print(*msg,sep="\n")
    return driver

def endInstance(driver):
  driver.quit()

def fileNameIfy(name):
    name=name.replace('/','-')
    nn="".join(x for x in name if x not in "\:*?<>|")
    return str(nn)


def readQuizToCsv(d):
    msg=[]
    try:
        title=fileNameIfy(d.find_element(By.XPATH, "//textarea[@name='Theme']").text)
        #msg.append(f"Got Title: {title}")
        if "Zeno" in title:
            msg.append("We don't talk about Zeno")
            return msg,title
        quizRecord="archive/"+title+"/"+title+".csv"
        if os.path.exists(quizRecord):
            msg.append("Don't worry,be happy")
            return msg,title
        os.makedirs(os.path.dirname(quizRecord), exist_ok=True)
        csv_file= open(quizRecord,"w",newline='')
        writer=csv.writer(csv_file, dialect='excel')
        d.find_element(By.XPATH, "//button[@data-tab-id='questions']").click()
        writer.writerow([title])
        writer.writerow(["Number","Question","CORRECT"])
        qLinks=d.find_elements(By.CSS_SELECTOR, ".menuItem--question") 
        d.implicitly_wait(0)
        for i in range(len(qLinks)-1):
            qText=d.find_element(By.NAME, "QuestionText").text
            if("CATEGORY" in qText):
                results=re.search(r'(CATEGORY.*?)\n*([A-Z]?[a-z]+.*)',qText,flags=re.MULTILINE|re.DOTALL)
                #msg.append(results.group(1))
                writer.writerow([results.group(1)])
                qText=results.group(2)

            answerNodes=d.find_elements(By.CSS_SELECTOR, ".answerList__textArea")
            correct=d.find_element(By.XPATH, "//textarea[ancestor::div[preceding-sibling::div/label/input[@checked]]]").text
            answers=[a.text for a in answerNodes]

            photoNode=d.find_elements(By.XPATH,"//div[@mediatype='Image']")
            if(photoNode):
                url=re.search(r'https.*800/.*\.[a-z]{2,4}',photoNode[0].get_attribute('style'))
                #msg.append(url.group(0))
                urllib.request.urlretrieve(url.group(0), "archive/"+title+"/"+str(i)+"-"+correct+".jpg")

            row=[i+1,qText,correct]+answers
            writer.writerow(row)
            qLinks[i+1].click()
        #csv_file.close()
    except Exception as err:
        #msg.append(f"Unexpected {err=}, {type(err)=}")
        raise err
    finally:
        return msg,title
    
    

def newThread(goTo,newD,i):
    msg=[]
    try:
        newD.implicitly_wait(10)
        newD.get("https://myquiz.org/Lectures")
        newD.execute_script(goTo)
        newMs,title=readQuizToCsv(newD)
        msg=[f"COMPLETED: Quiz {i}   {title}"]+newMs
    except Exception as err:
        msg.append(f"Unexpected {err=}, {type(err)=}")
        msg=[f"FAILED: Quiz {i}"]+msg
    print(*msg,sep="\n")

def selectQuiz(d):
    listOfQuizes= d.find_elements(By.XPATH, "//div[@id='lectureList']//div[@class='gridTimeLine_row']")
    #print(len(listOfQuizes))
    quizLinks=[]
    for i in range(35,99):
        link=listOfQuizes[i].find_element(By.XPATH, ".//div[@class='lectureListItemButtons--desktop']/a")
        #print(link.get_attribute('onclick'))
        quizLinks.append(link.get_attribute('onclick'))
        #d.execute_script(quizLinks[i])
    workers=3
    with ThreadPoolExecutor(max_workers=workers) as executor:
        heads=[] #need the number of heads to be equal to 
        for i in range(workers):
            heads.append(executor.submit(setup).result())
        for i,l in enumerate(quizLinks):
            future = executor.submit(newThread,l,heads[i%workers],i)
        executor.shutdown(wait=True)
        for h in heads:
            h.close()
        