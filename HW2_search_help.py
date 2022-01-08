from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='/Users/rajni/PycharmProjects/cleaner-python-selenium-automation/python-selenium-automation/chromedriver')
driver.implicitly_wait(5)

driver.get('https://www.amazon.com/gp/help/customer/display.html')

driver.find_element(By.XPATH, "//span[@class='a-size-medium a-text-bold']")

search= driver.find_element(By.ID, 'helpsearch')
search.send_keys('Cancel order', Keys.ENTER)

actual_text = driver.find_element(By.XPATH, "//a[@name= 'GUID-159D403A-3B08-477C-88E3-58C737822D49']/../h1").text




