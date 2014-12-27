# Created by mervetuccar at 12/25/14
Feature: Add item to the shopping bag

  As a customer
  I would like to add as many as items to my shopping bag
  So that I can checkout and pay for them

  Scenario: Adding an item to the empty shopping bag
    Given An empty shopping bag
    When I add an item to the shopping bag
    Then The bag icon should show the number of the item
    And  I click on the bag icon
    Then The checkout drop down is displayed
    And  I click on the submit button
    Then The checkout form should be displayed

    #out of stock issues?

    #question: does each scenario perform one big task?
    #should I call this file checkout?
  #should I give specific numbers like below or say general like items
  Scenario: Checkout page using arrows to control number of items
    Given Checkout page with an item to checkout
    When I increase the number of items by 2 using arrow
    Then The total sum should be 3
    And I decrease the number of items using arrow
    Then The total sum should decrease

    #total sum =

  Scenario: Deleting an item
    Given A shopping bag with 2 items
    When I click on delete item button
    Then The number of items should be 1
    And I delete this item too
    Then The the shopping bag should become empty
    And I click on bag icon
    Then It should say No Item in Your Bag
    And I click on checkout button
    Then The message should say 'You need to add some items to your basket to checkout'
    And I click on continue shopping button
    Then I go back to main page
    #should I check navigation like this one above?

  Scenario: Checkout
    Given A shopping bag with items
    When I click on checkout button
    Then The payment form should be displayed


