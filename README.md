# PythonExam
Blackjack exam for Python KEA 2019

### Assignment 2 - Blackjack

## Setup
Follow the instructions, this will allow the project to be run on your PC: 
  1. Download the project .zip to your computer (Green button "Clone or download) https://github.com/C-Strunge/PythonExam
  2. Extract .zip file.
  3. Open your IDE(I use Visual Studio Code), click File --> Open, choose the project you just extracted.
  4. Make sure you're in the workspace ../Exam.
  5. Write: "python BlackjackFinal.py' in the terminal.

## Dealer
At the beginning of the game, you will have to decide if you will be the "Dealer" or the "Player" if you type "d" (for dealer),
the game will run as so:

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

Christian Møller Strunge / [C-Strunge](https://github.com/C-Strunge)
