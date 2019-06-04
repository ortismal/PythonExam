# PythonExam
Blackjack exam for Python KEA 2019

### Assignment 2 - Blackjack

## Setup

To run the application on your computer, follow the instructions below:
  1. Download the .zip project to your computer from this page: https://github.com/ortismal/PythonExam.
  2. Extract the .zip file.
  3. Open up your IDE (for example Visual Studio, or any other environment that can run Python).
  4. Navigate to the workspace '../PythonExam'.
  5. Open your terminal and write 'python BlackjackFinal.py' - this will start the program.

# An overview of the application:

## Dealer

When you start the game, you decide whether to play as a player, or the dealer. If you type 'd' for dealer, the game will run as such:

  1. Player turn will be played automatically, and the player bet is fixed (20) every turn.
  2. You will automatically hit if below 17. 
  3. Who wins/loses is shown
  4. Player balance is updated (depending on outcome). 
  5. Continue playing is asked, and you may type y/n for yes or no.

## Player
If you decide to type "p" (play as player), you will have the following options, and the game will run as so:

  1. Decide how much you want to bet, you cannot bet more than your balance (starts at 100)
  2. You are dealt two cards, and have to decide if you want to hit or stand.
  If you choose to "hit", another card will be added. 
  If you choose to "stand", your turn will end and the dealers will begin
  3. Once dealers turn is done, see 3 --> 4 --> 5 under the "Dealer" section

## Test

Follow the instruction below for testing of the program:

  1. Open the UnittestCases.py file (to see code) and type: python UnittestCases.py

## Built With

[Visual Studio Code](https://code.visualstudio.com)

## Author

Casper Frost Andersen / [ortismal](https://github.com/ortismal)
