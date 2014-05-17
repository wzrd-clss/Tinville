Feature: Designer Shop Color Selection

  In order to select a color for the designer shop
  As a designer
  I want to have a menu that allows me to choose a color for the shop

@yori
  Scenario: Color Menu
	Given a shop editor
	When the color tab is selected
	Then the color picker wheel is displayed
	And the color picker textbox is displayed
	And the create button is displayed


  Scenario: Color Menu Submit
    Given the colorpicker
    When the color is chosen
    The page refreshes
    And the selected color is applied to the components of the shop