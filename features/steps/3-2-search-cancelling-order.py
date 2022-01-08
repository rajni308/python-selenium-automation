from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


TEST_VALUE = "Cancel Items or Orders"


@given('Open Amazon Help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')
    sleep(2)


@when('Input {search_word} into search bar')
def find_search_and_input_text(context, search_word):
    search = context.driver.find_element(By.ID, 'helpsearch')
    search.clear()
    search.send_keys(search_word, Keys.ENTER)
    sleep(4)

@then('Search Result page is displayed')
def verify_search_result_page_displayed(context):
    text = context.driver.find_element(By.XPATH, "//a[@name= 'GUID-159D403A-3B08-477C-88E3-58C737822D49']/../h1").text
    print("extracted XPath text is : ",text)
    assert TEST_VALUE == text