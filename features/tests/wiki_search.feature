Feature: tests for Wikipedia search

  Scenario: User can search on Wikipedia
    Given Click to Skip onboarding
    When Click Search icon
    And Search for Python (programming language)
    Then Verify first result is Python (programming language)


Scenario: User can search on Wikipedia
    Given Click to Skip onboarding
    When Click Search icon
    And Search for Cartoon Network
    Then Verify first result is Cartoon Network


  Scenario: User can search on Wikipedia
    Given Click to Skip onboarding
    When Click Search icon
    And Search for Jesus Christ
    Then Verify first result is Jesus Christ


 Scenario: User can search on Wikipedia
    Given Click to Skip onboarding
    When Click Search icon
    And Search for Africa
    Then Verify first result is Africa


