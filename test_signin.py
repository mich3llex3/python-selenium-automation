#=======Locators=====
#Element: Amazon Logo
#Strategy: XPATH
#Value://i[@aria-label= 'Amazon']

#Element: Email Field
#Strategy: ID
#Value: ap_email_

#Element: Continue Button
#Strategy: ID
#Value: continue

#Element: Conditions of Use link
#Strategy: LINK TEXT
#Value: Conditions of Use

#Element: Privacy Notice link
#Strategy: LINK TEXT
#Value: Privacy Notice

#Element:Need help link
#Strategy: LINK TEXT
#Value: Need help?

#Element:Forgot your password link
#Strategy: LINK TEXT
#Value: Forgot your password?

#Element: Other issues with Sign-In link
#Strategy: LINK TEXT
#Value: Other issues with Sign-In

#Element:Create your Amazon account button
#Strategy:LINK TEXT
#Value: Create a free business account

#===========TEST CASE============
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.target.com/')
driver.find_element(By.LINK_TEXT,'Account').click()

sleep(5)

driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

sleep(5)

