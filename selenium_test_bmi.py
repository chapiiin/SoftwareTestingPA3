from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


def test_bmi():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options)
                          
    #open the calculator
    driver.get('https://bmiretirementcalculator.000webhostapp.com/')

    #fill out BMI test 1 info
    time.sleep(1)
    feet1 = driver.find_element_by_xpath("//*[@id='height_ft']")
    feet1.send_keys('5')
    inch1 = driver.find_element_by_xpath("//*[@id='height_in']")
    inch1.send_keys('3')
    weight1 = driver.find_element_by_xpath("//*[@id='weight']")
    weight1.send_keys('100')
    #click calculate BMI button
    driver.find_element_by_xpath("/html/body/div/div[1]/div[4]/button").click()

    #find BMI 1
    for ele in driver.find_elements_by_xpath('.//span[@id = "bmi"]'):
        bmi1 = ele.text
    print("Bmi1: ", bmi1, end = " ")
    #find BMI 1 category
    for ele in driver.find_elements_by_xpath('.//span[@id = "bmi_category"]'):
        bmi1_category = ele.text
    print("Bmi1 Category: ", bmi1_category)

    #check if test 1 passed
    if ((bmi1 == '18.1') and (bmi1_category == 'Underweight')):
        test1 = True

    #clear text boxes
    feet1.clear()
    inch1.clear()
    weight1.clear()
    time.sleep(1)


    #fill out BMI test 2 info
    feet2 = driver.find_element_by_xpath("//*[@id='height_ft']")
    feet2.send_keys('5')
    inch2 = driver.find_element_by_xpath("//*[@id='height_in']")
    inch2.send_keys('3')
    weight2 = driver.find_element_by_xpath("//*[@id='weight']")
    weight2.send_keys('125')
    #click calculate BMI button
    driver.find_element_by_xpath("/html/body/div/div[1]/div[4]/button").click()

    #find BMI 1
    for ele in driver.find_elements_by_xpath('.//span[@id = "bmi"]'):
        bmi2 = ele.text
    print("Bmi2: ", bmi2, end = " ")
    #find BMI 1 category
    for ele in driver.find_elements_by_xpath('.//span[@id = "bmi_category"]'):
        bmi2_category = ele.text
    print("Bmi2 Category: ", bmi2_category)

    #check if test 2 passed
    if ((bmi2 == '22.7') and (bmi2_category == 'Normal weight')):
        test2 = True

    #clear text boxes
    feet2.clear()
    inch2.clear()
    weight2.clear()
    time.sleep(1)


    #fill out BMI test 3 info
    feet3 = driver.find_element_by_xpath("//*[@id='height_ft']")
    feet3.send_keys('5')
    inch3 = driver.find_element_by_xpath("//*[@id='height_in']")
    inch3.send_keys('3')
    weight3 = driver.find_element_by_xpath("//*[@id='weight']")
    weight3.send_keys('150')
    #click calculate BMI button
    driver.find_element_by_xpath("/html/body/div/div[1]/div[4]/button").click()

    #find BMI 3
    for ele in driver.find_elements_by_xpath('.//span[@id = "bmi"]'):
        bmi3 = ele.text
    print("Bmi3: ", bmi3, end = " ")
    #find BMI 3 category
    for ele in driver.find_elements_by_xpath('.//span[@id = "bmi_category"]'):
        bmi3_category = ele.text
    print("Bmi3 Category: ", bmi3_category)

    #check if test 3 passed
    if ((bmi3 == '27.2') and (bmi3_category == 'Overweight')):
        test3 = True

    #clear text boxes
    feet3.clear()
    inch3.clear()
    weight3.clear()
    time.sleep(1)

    #fill out BMI test 4 info
    feet4 = driver.find_element_by_xpath("//*[@id='height_ft']")
    feet4.send_keys('5')
    inch4 = driver.find_element_by_xpath("//*[@id='height_in']")
    inch4.send_keys('3')
    weight4 = driver.find_element_by_xpath("//*[@id='weight']")
    weight4.send_keys('175')
    #click calculate BMI button
    driver.find_element_by_xpath("/html/body/div/div[1]/div[4]/button").click()

    #find BMI 4
    for ele in driver.find_elements_by_xpath('.//span[@id = "bmi"]'):
        bmi4 = ele.text
    print("Bmi4: ", bmi4, end = " ")
    #find BMI 4 category
    for ele in driver.find_elements_by_xpath('.//span[@id = "bmi_category"]'):
        bmi4_category = ele.text
    print("Bmi4 Category: ", bmi4_category)

    #check if test 4 passed
    if ((bmi4 == '31.7') and (bmi4_category == 'Obese')):
        test4 = True

    #check if all tests passed
    if (test1 and test2 and test3 and test4):
        print("*ALL TESTS PASSED*")
    time.sleep(5)

test_bmi()
