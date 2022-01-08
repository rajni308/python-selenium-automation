from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


TEST_VALUE = "Your Amazon Cart is empty"


@given('Open Amazon page_3_3')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')
    #sleep(2)


@when('Select cart from the page')
def find_cart_icon_on_page(context):
    cart = context.driver.find_element(By.XPATH, "//span[@class = 'nav-cart-icon nav-sprite']")
    cart.click()
    sleep(4)

@then('Cart is empty')
def verify_cart_is_empty(context):
    text_in_the_cart = context.driver.find_element(By.XPATH, "//h2").text
    print("extracted XPath text is : ",text_in_the_cart)
    assert TEST_VALUE == text_in_the_cart