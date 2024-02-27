# simulated-uno

This is a project from my Intro to Software Engineering class.
Simulated Uno is a simplified version of the uno game. It creates and runs a 
simulated game between npc players based on values given by the user. The
moves and results are printed in the terminal.

## Installation

Download and extract the project from github

## Usage

Use Intellij to open the Uno folder. Go to the RunOneGame class to run a single game.
Input the values you want to create the game.

#### Values to create the game:
* countPlayers — number of players
* countInitialCardsPerPlayer — number of cards initially dealt to each player
* countDigitCardsPerColor — number of normal cards for each digit and color.
  * For example, 2 means 2 Blue “0” cards, 2 Green “0” cards, 2 Yellow "0" cards, 2 Red "0" cards,
    2 Blue "1" cards, 2 Green "1" cards, etc.
* countSpecialCardsPerColor — number of special cards of each kind for each color.
   * For example, 1 means 1 Red Skip card, 1 Yellow Skip card, ..., 1 Red Reverse card, 1 Yellow Reverse card, etc.
     May be 0. There are is only Skip, Reverse and Draw 2.
* countWildCards — number of total wild cards. May be 0.

## Modified Rules:
Simplified version of uno. Follows the standard rules with the modifications below:<br />

#### Taking a turn:<br />
If a player has any playable card, they must play one of them and then their turn ends. 
If they don’t have any playable cards, then they must draw a card from the draw pile. 
If the card drawn is playable, they must play it immediately. 
Otherwise, they add the card to their hand and their turn ends.<br />

#### Cards:<br />
Wild card: The card has  no color until a player declares the color when they play it.<br />
Normal card: The card has a color(blue, red, yellow, green) and either a digit(0-9) or a special instruction.
Special instructions:
* Skip: The next player is skipped.
* Reverse: The order of play is reversed.
* Draw Two: The next player must draw two cards and then their turn is over.<br />

#### Playable Cards:<br />
A card is playable if it can be put on top of the discard pile.
* A normal card is playable if it matches the color or the face of the card on top of the discard pile.
  Ex: Blue-3 can be played on top of a Blue-3, Blue-Skip, Yellow-3, but not on a Green-1.
* A wild card is always playable. If it is on top of the discard pile, it is treated as whatever color the player chose it to be.<br />

#### Running out of draw cards:<br />
If the draw pile is empty, the discard pile replaces it.
* The top of the discard pile is retained as the start of the new discard pile. The other cards are shuffled and used as the draw pile.
