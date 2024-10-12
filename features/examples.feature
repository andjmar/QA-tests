Feature: Create a new project

  @test1
  Scenario: Successfull form submitting
    Given I am on the home page
    When I enter the name, email and password
    And I click on the checkbox
    And I select option Female and Student
    And I enter the date
    Then I click on the submit button and check the success message

  @test2
  Scenario: Order placing
    Given I am on the GreenKart page
    When I search for the product
    And I add the products to the cart
    And I enter the promo code
    Then I select the country, check the checkbox and click on the purchase button
