from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium .webdriver.common.by import By
import time

# driver = webdriver.Chrome()

driver = webdriver.Chrome(executable_path='/Users/rajni/PycharmProjects/driver/chromedriver')
driver.maximize_window()
# driver.implicitly_wait(4)


# open the url
driver.get('https://www.google.com/')
driver.maximize_window()

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('table')

# # wait for 4 sec
# sleep(4)
driver.wait = WebDriverWait(driver, 10)


# click search
# driver.find_element(By.NAME, 'btnK').click()

element = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Search button not found')
element.click()



# verify
assert 'table' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()

