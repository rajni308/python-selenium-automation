# Created by rajni at 1/16/22
Feature: test your empty cart has items that are added

  Scenario: check your empty cart has items that are added
    Given Open Amazon cart page
    When Check Your Amazon Cart is empty
    When Search table on the search bar
    And Click the first item
    And Add to cart first item
    And installation pop up window shows
    And Close the pop up window
    Then Check your cart has added item