from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5) # applied to all find_element(s) => check for E every 100ms
driver.wait = WebDriverWait(driver, timeout=10) # applied to wait.until(), waits for condition to be met every 1/2 sec

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

search_btn = (By.NAME, 'btnK')
driver.wait.until(EC.element_to_be_clickable(search_btn), message='Search button not clickable').click()

# verify
driver.wait.until(EC.url_contains('Dress'), message=f"Expected query not in {driver.current_url}")
# assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()