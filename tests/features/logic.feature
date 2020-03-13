# Created by jennifer.riordan at 13/03/2020
Feature: Game logic

  Background: There is a 6 x 7 game board of zeros
    Given The board is initialized

  Scenario: Player 1 makes the first move
    Given The board contains only zeros
    When #Player 1 chooses where to put their game piece
    Then #the board updates with the number 1 where Player 1 moved

 # Scenario: Player 2 makes their first move
    Given #Player 1 has taken their turn
    When #Player 2 chooses where to put their game piece
    Then #the board updates to reflect both Player 1 and Player 2 have moved