# Amazon logo
driver.find_element(By.XPATH,"//i[@class= 'a-icon a-icon-logo']")

# Email field
driver.find_element(By.Id('ap_email').sendkeys('text'))

# continue button
driver.find_element(By.Id('continue'))

# Need help button
driver.find_element(By.XPATH,"//span[@class= 'a-expander-prompt']")

# Forgot your password link
driver.find_element(By.Id('auth-fpp-link-bottom'))

# Other issues with sign in link
driver.find_element(By.Id('ap-other-signin-issues-link'))

#Create your amazon account button
driver.find_element(By.Id('createAccountSubmit'))

# conditions of use link
driver.find_element(By.XPATH,"//a[@href= '/gp/help/customer/display.html/ref=ap_signin_
                             notification_condition_of_use?ie=UTF8&nodeId=508088']")
# privacy notice link
driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_signin_
notification_privacy_notice?ie=UTF8&nodeId=468496']")


