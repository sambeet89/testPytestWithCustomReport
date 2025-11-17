
Feature: this is a test festure

  Background: test bck ground
    Given we are executing background



    @regression2
    Scenario Outline:
      Given we ar ein the testoutline with example
      When the testdata is <data>
      And add 10 to the data
      Then lets print the output designed for multiply 
      Examples:
        |data|
        |10|
        |20|

