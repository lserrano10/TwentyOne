Steps to play the game:

1. Create a deck of 52 cards
2. Shuffle the deck
3. Ask the player for their bet
4. Make sure that the Player’s bet does not exceed their available chips
5. Deal two cards to the Dealer and two cards to the Player
6. Show only one of the Dealer’s cards, the other remains hidden
7. Show both of the Player’s cards
8. Ask the Player if they wish to Hit, and take another card
9. If the Player’s hand doesn’t Bust (go over 21), ask if they’d like to Hit again.
10. If a Player Stands, play the Dealer’s hand. The dealer will always Hit until the Dealer’s value meets or exceeds 17
11. Determine the winner and adjust the Player’s chips accordingly
12. Ask the Player if they’d like to play again

Playing Cards

A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and thirteen values (2 through 10, Jack, Queen, King and Ace) which makes a total of 52 cards per deck. Jacks, Queens and Kings all have different value. Jack is 1 point, Queen 2 points and King 3 points. Aces have a value of either 11 or 1 as needed to reach 21 without busting. The Joker does not play.


The game


Step 1: Import and Global Variables

Import the random module, to shuffle the deck before dealing.
Declare variables to store suits, ranks and values.
Declare a Boolean value to be used to control while loops to control the flow of the game.


Step 2: Create a Card Class

A card object really only needs two attributes: suit and rank.
In addition to the Card’s __init__ method, consider adding a __str__ method that, when asked to print a Card, returns a string in the form “Two of Hearts”


Step 3: Create a Deck Class

Here we might store 52 card objects in a list that can later be shuffled.
First, instantiate all 52 unique card objects and add them to the list.
Consider iterating over sequences of suits and ranks to build out each card. This might appear inside a Deck class __init__ method.
In addition to an __init__ method we’ll want to add methods to shuffle our deck, and to deal out cards during gameplay.


Step 4: Create a Hand Class

In addition to holding Card objects dealt from the Deck, the Hand class may be used to calculate the value of those cards using the values dictionary defined above. It may also need to adjust for the value of Aces when appropriate.


Step 5: Create a Chips Class

To keep track of a Player’s starting chips, bets, and ongoing winnings.


Step 6: Write a function for taking bets

Since we’re asking the user for an integer value, this would be a good place to use try/except. Remember to check that a Player's bet can be covered by their available chips.
We used a while loop here to continually prompt the user for input until we received an integer value that was within the Player's betting limit.


Step 7: Write a function for taking hits

Either player can take hits until they bust. This function will be called during gameplay anytime a Player requests a hit or a Dealer’s hand is less than 17. It should take in Deck and Hand objects as arguments, and deal one card off the deck and add it to the Hand. You may want it to check for aces in the event that a player’s hand exceeds 21.


Step 8: Write a function prompting the Player to Hit or Stand

This function should accept the deck and the player’s hand as arguments, and assign playing as a global variable.
If the Player Hits, employ the hit() function above. If the Player Stands, set the playing variable to False — this will control the behaviour of a while loop later on in our code.


Step 9: Write functions to display cards

When the game starts, and after each time Player takes a card, the dealer’s first card is hidden and all of Player’s cards are visible. At the end of the hand, all cards are shown, and you may want to show each hand’s total value. Write a function for each of these scenarios.


Step 10: Write functions to handle end of game scenarios

Remember to pass a player’s hand, dealer’s hand and chips as needed.
