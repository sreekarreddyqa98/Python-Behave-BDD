Feature: Validation of the Login Functionality

  @one
  Scenario: Validating Login woth a single Valid Username and Password
    Given I navigate to "LOGIN_PAGE"
    When I enter "Admin" in the "USERNAME_TXTBOX" field
    And I enter "admin123" in the "PASSWORD_TEXTBOX" field
    And I click on the "LOGIN" button
    Then I should be in "DASBOARD" page

  @two
  Scenario Outline: Validating Login woth a single Valid Username and Password 2
    Given I navigate to "LOGIN_PAGE"
    When I enter "<username>" in the "USERNAME_TXTBOX" field
    And I enter "<password>" in the "PASSWORD_TEXTBOX" field
    And I click on the "LOGIN" button
    Then I should be in "DASBOARD" page

    Examples:
      | username | password |
      | sreekar  | 123456   |
      | reddy    | 56789    |
      | Admin    | admin123 |