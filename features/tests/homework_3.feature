Feature: Test Scenarios for Homework 3

  Scenario: User can see 'Your cart is empty' message
  Given Open Target main page
  When Click on cart icon
  Then Verify 'Your cart is empty' message is shown

  Scenario: Logged out user can navigate to Sign In
  Given Open Target main page
  When Click on account icon
  Then Click on 'Sign in or create account' button
  Then Verify Sign in form opened

