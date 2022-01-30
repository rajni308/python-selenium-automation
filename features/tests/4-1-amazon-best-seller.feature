# Created by rajni at 1/8/22
Feature: # Amazon home page Tests
  # Enter feature description here

  Scenario: # Check for Best Sellers on Amazon HomePage has 5 links
    Given Open Best Sellers page
    Then Assert there are 5 subtabs

