Feature: Test cases for Product Search on Target

  Scenario: User can search for a product "tea" on Target
    Given Open Target main page
    When Search for tea
    Then Verify search results for tea shown

  Scenario: User can search for a product "coffee" on Target
    Given Open Target main page
    When Search for coffee
    Then Verify search results for coffee shown

  Scenario Outline: User can search for products
    Given Open Target main page
    When Search for <search_query>
    Then Verify search results for <product> shown
    Examples:
    |search_query   |product      |
    |Coffee         |Coffee       |
    |coffee cup     |coffee cup   |
    |sugar          |sugar        |
#    |茶             |茶           |

Scenario: Verify that user can see product names and images
  Given Open Target main page
  When Search for Airpods
  Then Verify that every product has a name and an image
  