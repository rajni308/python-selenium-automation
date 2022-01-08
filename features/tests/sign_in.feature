# Created by rajni at 12/26/21
Feature: sign in tests
 1. Open https://www.amazon.com
 2. Click Orders
 3. Verify Sign in page opened


  Scenario: user can see sign page
    Given Open Amazon page
    When Click Orders
    Then verify Sing in page opened