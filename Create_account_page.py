from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='/Users/rajni/PycharmProjects/cleaner-python-selenium-automation/python-selenium-automation/chromedriver')

driver.implicitly_wait(5)

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//div[@class = 'a-section a-padding-medium auth-workflow']")

driver.find_element(By.ID,'createAccountSubmit').click()
driver.implicitly_wait(5)

# BY XPATH (Amazon logo on the create account page)
driver.find_element(By.XPATH,"//i[@class = 'a-icon a-icon-logo']")

# BY XPATH ( create account)
driver.find_element(By.XPATH,"//h1[@class = 'a-spacing-small']")

# BY ID (your name )
driver.find_element(By.ID,'ap_customer_name')

# BY XPATH (your name)
driver.find_element(By.XPATH,"//input[@Id = 'ap_customer_name']")

# BY XPATH (email field)
driver.find_element(By.XPATH,"//input[@id = 'ap_email']")

# BY XPATH (password field)
driver.find_element(By.XPATH,"//input[@id = 'ap_password']")

# BY XPATH (Re-enter password)
driver.find_element(By.XPATH,"//input[@id = 'ap_password_check']")

# BY XPATH (create your amazon account)
driver.find_element(By.XPATH,"//input[@id = 'continue']")

# using tag[atribute = value] (CSS SELECTOR)
driver.find_element(By.CSS_SELECTOR,"a[href*='ap_register_notification_condition_of_use']")

# using tag[atribute = value] (CSS SELECTOR)
driver.find_element(By.CSS_SELECTOR,"a[href ='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&amp;nodeId=468496']")







