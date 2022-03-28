from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')

SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')

@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')



@then('Verify user can click through colors')
def verify_can_click_colors(context):

    expected_colors = ['Army Green', 'Black', 'Blue']
    colors = context.driver.find_elements(*COLOR_OPTIONS)


    actual_colors = []

    for color in colors[:3]:

        color.click()
        actual_colors += [context.driver.find_element(*SELECTED_COLOR).text]

        print(actual_colors)

    assert actual_colors == expected_colors, f'Expected {expected_colors} but got {actual_colors}'