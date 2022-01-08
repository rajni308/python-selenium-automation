# Created by Rajni
Feature: Test Scenario for empty cart in amazon

  Scenario: User searches for cart is empty on amazon
    Given Open Amazon page_3_3
    When Select cart from the page
    Then Cart is empty

