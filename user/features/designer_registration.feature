Feature: Designer Registration

  As a Designer
  I would like to register as a designer on Tinville
  So that I may use all of the features on Tinville, including opening up a Shop

  @wip
  Scenario: Form entry
	When I register for a shop named "foo"
	Then I can visit my shop at "/foo/"
