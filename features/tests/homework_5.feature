Feature: Test Scenarios for Homework 5

  Scenario: User can see story cards on Target Circle page
  Given Open Target Circle page
  Then Verify Target Circle has two story cards

  Scenario: User can add product to cart
    Given Open Target home page
    When Search for pillow
    Then Select product to add

 Scenario: Verify product colors
   Given Open blouse product page
   Then Verify all colors can be selected
