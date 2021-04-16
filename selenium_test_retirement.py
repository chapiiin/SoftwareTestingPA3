from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


def test_retirement():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options)
                          
    #open the calculator
    driver.get('https://bmiretirementcalculator.000webhostapp.com/')

    #fill out Retirement test 1 info
    time.sleep(1)
    age1 = driver.find_element_by_xpath("//*[@id='age']")
    age1.send_keys('25')
    sal1 = driver.find_element_by_xpath("//*[@id='salary']")
    sal1.send_keys('70000')
    per1 = driver.find_element_by_xpath("//*[@id='saved']")
    per1.send_keys('10.5')
    goal1 = driver.find_element_by_xpath("//*[@id='goal']")
    goal1.send_keys('500000')
    #click calculate retirement button
    driver.find_element_by_xpath("/html/body/div/div[2]/div[5]/button").click()

    #find retirement goal
    for ele in driver.find_elements_by_xpath('.//span[@id = "retirement_age"]'):
        r_age1 = ele.text
    print("Retirement age 1: ", r_age1, end = " ")
    #find if retirement 1 goal met
    for ele in driver.find_elements_by_xpath('.//span[@id = "goal_met"]'):
        met1 = ele.text
    print("Goal 1 met: ", met1)

    #check if test 1 passed
    if ((r_age1 == '76') and (met1 == 'be met')):
        print("Test 1 passed")
        test1 = True

    #clear text boxes
    age1.clear()
    sal1.clear()
    per1.clear()
    goal1.clear()

    #fill out Retirement test 2 info
    age2 = driver.find_element_by_xpath("//*[@id='age']")
    age2.send_keys('25')
    sal2 = driver.find_element_by_xpath("//*[@id='salary']")
    sal2.send_keys('70000')
    per2 = driver.find_element_by_xpath("//*[@id='saved']")
    per2.send_keys('10.5')
    goal2 = driver.find_element_by_xpath("//*[@id='goal']")
    goal2.send_keys('9000')
    #click calculate retirement button
    driver.find_element_by_xpath("/html/body/div/div[2]/div[5]/button").click()

    #find retirement goal
    for ele in driver.find_elements_by_xpath('.//span[@id = "retirement_age"]'):
        r_age2 = ele.text
    print("Retirement age 2: ", r_age2, end = " ")
    #find if retirement 2 goal met
    for ele in driver.find_elements_by_xpath('.//span[@id = "goal_met"]'):
        met2 = ele.text
    print("Goal 2 met: ", met2)

    #check if test 2 passed
    if ((r_age2 == '26') and (met2 == 'be met')):
        print("Test 2 passed")
        test2 = True

    #clear text boxes
    age2.clear()
    sal2.clear()
    per2.clear()
    goal2.clear()
    time.sleep(2)

    #fill out Retirement test 3 info
    age3 = driver.find_element_by_xpath("//*[@id='age']")
    age3.send_keys('20')
    sal3 = driver.find_element_by_xpath("//*[@id='salary']")
    sal3.send_keys('100000')
    per3 = driver.find_element_by_xpath("//*[@id='saved']")
    per3.send_keys('15')
    goal3 = driver.find_element_by_xpath("//*[@id='goal']")
    goal3.send_keys('1000000')
    #click calculate retirement button
    driver.find_element_by_xpath("/html/body/div/div[2]/div[5]/button").click()

    #find retirement goal
    for ele in driver.find_elements_by_xpath('.//span[@id = "retirement_age"]'):
        r_age3 = ele.text
    print("Retirement age 3: ", r_age3, end = " ")
    #find if retirement 3 goal met
    for ele in driver.find_elements_by_xpath('.//span[@id = "goal_met"]'):
        met3 = ele.text
    print("Goal 3 met: ", met3)

    #check if test 3 passed
    if ((r_age3 == '70') and (met3 == 'be met')):
        print("Test 3 passed")
        test3 = True

    #clear text boxes
    age3.clear()
    sal3.clear()
    per3.clear()
    goal3.clear()

    #fill out Retirement test 4 info
    age4 = driver.find_element_by_xpath("//*[@id='age']")
    age4.send_keys('50')
    sal4 = driver.find_element_by_xpath("//*[@id='salary']")
    sal4.send_keys('85000')
    per4 = driver.find_element_by_xpath("//*[@id='saved']")
    per4.send_keys('12.7')
    goal4 = driver.find_element_by_xpath("//*[@id='goal']")
    goal4.send_keys('1234567')
    #click calculate retirement button
    driver.find_element_by_xpath("/html/body/div/div[2]/div[5]/button").click()

    #find retirement goal
    for ele in driver.find_elements_by_xpath('.//span[@id = "retirement_age"]'):
        r_age4 = ele.text
    print("Retirement age 4: ", r_age4, end = " ")
    #find if retirement 4 goal met
    for ele in driver.find_elements_by_xpath('.//span[@id = "goal_met"]'):
        met4 = ele.text
    print("Goal 4 met: ", met4)

    #check if test 4 passed
    if ((r_age4 == '100') and (met4 == 'not be met')):
        print("Test 4 passed")
        test4 = True

    #clear text boxes
    age4.clear()
    sal4.clear()
    per4.clear()
    goal4.clear()

    #fill out Retirement test 5 info
    age5 = driver.find_element_by_xpath("//*[@id='age']")
    age5.send_keys('27')
    sal5 = driver.find_element_by_xpath("//*[@id='salary']")
    sal5.send_keys('65000')
    per5 = driver.find_element_by_xpath("//*[@id='saved']")
    per5.send_keys('7')
    goal5 = driver.find_element_by_xpath("//*[@id='goal']")
    goal5.send_keys('750000')
    #click calculate retirement button
    driver.find_element_by_xpath("/html/body/div/div[2]/div[5]/button").click()

    #find retirement goal
    for ele in driver.find_elements_by_xpath('.//span[@id = "retirement_age"]'):
        r_age5 = ele.text
    print("Retirement age 5: ", r_age5, end = " ")
    #find if retirement 5 goal met
    for ele in driver.find_elements_by_xpath('.//span[@id = "goal_met"]'):
        met5 = ele.text
    print("Goal 5 met: ", met5)

    #check if test 5 passed
    if ((r_age5 == '100') and (met5 == 'not be met')):
        print("Test 5 passed")
        test5 = True

    #clear text boxes
    age5.clear()
    sal5.clear()
    per5.clear()
    goal5.clear()

    #fill out Retirement test 6 info
    age6 = driver.find_element_by_xpath("//*[@id='age']")
    age6.send_keys('16')
    sal6 = driver.find_element_by_xpath("//*[@id='salary']")
    sal6.send_keys('23550')
    per6 = driver.find_element_by_xpath("//*[@id='saved']")
    per6.send_keys('15')
    goal6 = driver.find_element_by_xpath("//*[@id='goal']")
    goal6.send_keys('1500000')
    #click calculate retirement button
    driver.find_element_by_xpath("/html/body/div/div[2]/div[5]/button").click()

    #find retirement goal
    for ele in driver.find_elements_by_xpath('.//span[@id = "retirement_age"]'):
        r_age6 = ele.text
    print("Retirement age 6: ", r_age6, end = " ")
    #find if retirement 6 goal met
    for ele in driver.find_elements_by_xpath('.//span[@id = "goal_met"]'):
        met6 = ele.text
    print("Goal 6 met: ", met6)

    #check if test 6 passed
    if ((r_age6 == '100') and (met6 == 'not be met')):
        print("Test 6 passed")
        test6 = True

    #clear text boxes
    age6.clear()
    sal6.clear()
    per6.clear()
    goal6.clear()

    #check if all tests passed
    if (test1 and test2 and test3 and test4 and test5 and test6):
        print("*ALL TESTS PASSED*")
    time.sleep(5)

test_retirement()
