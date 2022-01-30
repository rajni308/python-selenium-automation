from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# BEST_SELLER_TABS = (By.ID, "zg_header a") im getting 0 count here for somereason.

CART_EMPTY_TEXT_LOCATION = (By.XPATH, "//div[@id='sc-active-cart']//h2")
AMAZON_CART_URL = "https://www.amazon.com/gp/cart/view.html?ref_=nav_cart"

SEARCH_BAR_LOCATION = (By.ID, "twotabsearchtextbox")


FIRST_ITEM = (By.XPATH, "//div[@class = 'a-section a-spacing-none a-spacing-top-small s-title-instructions-style']//span[text()= 'Marco Group 24x48 Dry Erase/Gray Table']")


@given('Open Amazon cart page')
def open_amazon_cart_page(context):
    context.driver.get(AMAZON_CART_URL)


@when('Check {expected_empty_cart_txt}')
def check_cart_empty(context, expected_empty_cart_txt):
    actual_txt = context.driver.find_element(*CART_EMPTY_TEXT_LOCATION).text
    assert expected_empty_cart_txt == actual_txt, \
        f'Expected {expected_empty_cart_txt} did not match {actual_txt}'


@when('Search {search_text} on the search bar')
def search_item_in_the_bar(context, search_text):
    search = context.driver.find_element(*SEARCH_BAR_LOCATION)
    search.clear()
    search.send_keys(search_text, Keys.ENTER)
    # sleep(4)


@when('Click the first item')
def click_first_item(context):
    context.driver.find_element(*FIRST_ITEM).click()


@when('Add to cart first item')
def add_to_cart_item(context):
    context.driver.find_element(By.XPATH, "//input[@id = 'add-to-cart-button']").click()


@when('installation pop up window shows')
def installation_pop_up_window_shows(context):
    context.driver.find_element(By.XPATH, "//div[@class= 'a-popover-wrapper']")


@when('Close the pop up window')
def close_the_pop_up_window(context):
    # $x("//button[@data-action = 'a-popover-close']")
    context.driver.find_element(By.XPATH, "//button[@data-action = 'a-popover-close']").click()
    #sleep(4)


@then('Check your cart has added item')
def check_your_cart(context):
    counter = context.driver.find_element(By.XPATH, "//span[@id= 'nav-cart-count']")
    print("rajni is printing this element", counter)
    #TODO : i have to understand how to grab the value from the web-element. everything else is good.
    assert (counter != "null")
