from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
# ADD_TO_CART_BTN = (By.ID, 'add_to_cart_button')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')

@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')

# @when('Click on Add to Cart button')
# def click_add_to_cart(context):
  #  context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Verify user can click through colors')
def verify_can_click_colors(context):

    expected_colors = ['Army Green', 'Black', 'Blue']  # , 'Brown', 'Burgundy', 'Caramel', 'Dark Blue', 'Denim Blue', 'Gray', 'Green', 'Khaki', 'Light-green', 'Pink', 'Purple', 'Red', 'Rose Red', 'White', 'Yellow']

    colors = context.driver.find_elements(*COLOR_OPTIONS)

   # for i in range(len(colors)):
    #    colors[i].click()

   # actual_color = context.driver.find_element(*SELECTED_COLOR).text

  #  assert actual_color == expected_colors[i], f'Expected {expected_colors[i]}, but got {actual_color}'

    actual_colors = []

    for color in colors[:3]:

        color.click()
        actual_colors += [context.driver.find_element(*SELECTED_COLOR).text]

        print(actual_colors)

    assert actual_colors == expected_colors, f'Expected {expected_colors} but got {actual_colors}'