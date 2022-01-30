from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# BEST_SELLER_TABS = (By.ID, "zg_header a") im getting 0 count here for somereason.

BEST_SELLER_TABS = (By.XPATH, "//*[@id='zg_header']/div/div/div/ul/li")
BESET_SELLER_URL = "https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers"


@given('Open Best Sellers page')
def open_best_seller_page(context):
    context.driver.get(BESET_SELLER_URL)


@then('Assert there are {tabsCount} subtabs')
def assert_subtabs(context, tabsCount):

    subtabs_count = len(context.driver.find_elements(*BEST_SELLER_TABS))
    print(" the count is :", subtabs_count)
    print(" expected count is :", tabsCount)
    expected_count = int(tabsCount)
    assert expected_count == subtabs_count, \
        f'Expected {expected_count} did not match {subtabs_count}'
