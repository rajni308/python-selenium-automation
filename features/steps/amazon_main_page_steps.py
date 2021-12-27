from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when ('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@then('Verify Sign in page opened')
def verify_signin_opened(context):
    context.driver.find_element(By.ID, 'ap_email')
    expected_header = 'Sign-In'
    actual_header = context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").text
    assert expected_header == actual_header, f'Error! Expected {expected_header} but got {actual_header}'