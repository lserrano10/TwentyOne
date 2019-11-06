import io
import sys
import unittest
from twentyone_game import Card
from twentyone_game import Deck
from twentyone_game import Hand
from twentyone_game import Chips
from twentyone_game import show_some
from twentyone_game import take_bet


class TestTwentyOne(unittest.TestCase):

    def test_card_init(self):
        try:
            card = Card("Hearts", "Two")
        except ExceptionType:
            self.fail("Unable to initialize a `Card` object, exception thrown")

    def test_card_init2(self):
        out = io.StringIO()
        sys.stdout = out

        card1 = Card("Spades", "Two")
        print(card1)
        output = out.getvalue().strip()
        ps1 = "Two of Spades"
        self.assertEqual(output, ps1)
        out.truncate(0)
        out.seek(0)

        card2 = Card("Diamonds", "King")
        print(card2)
        output = out.getvalue().strip()
        ps2 = "King of Diamonds"
        self.assertEqual(output, ps2)
        out.truncate(0)
        out.seek(0)

        card3 = Card("Hearts", "Ace")
        print(card3)
        output = out.getvalue().strip()
        ps3 = "Ace of Hearts"
        self.assertEqual(output, ps3)
        out.truncate(0)
        out.seek(0)

        card4 = Card("Clubs", "Five")
        print(card4)
        output = out.getvalue().strip()
        ps4 = "Five of Clubs"
        self.assertEqual(output, ps4)

        out.close

    def test_deck_init(self):
        deck = Deck()
        self.assertEqual(len(deck.deck), 52)

    def test_deck_deal(self):
        deck = Deck()
        deck.deal()
        self.assertEqual(len(deck.deck), 51)

    def test_deck_dealHalf(self):
        deck = Deck()
        for i in range(1, 38):
            deck.deal()
        self.assertEqual(len(deck.deck), 15)

    def test_deck_shuffle(self):
        deck1 = Deck()
        deck2 = Deck()
        deck3 = Deck()
        deck1.shuffle()
        deck2.shuffle()
        deck3.shuffle()
        card1 = deck1.deck.pop(0)
        card2 = deck2.deck.pop(0)
        card3 = deck3.deck.pop(0)
        if card1 == card2 and card1 == card3:
            self.fail("The decks were not well shuffled")

    def test_hand_value1(self):
        playersHand = Hand()
        playersHand.add_card(Card("Clubs", "King"))
        playersHand.add_card(Card("Hearts", "Three"))
        self.assertEqual(6, playersHand.value)

    def test_hand_value2(self):
        playersHand = Hand()
        playersHand.add_card(Card("Clubs", "King"))
        playersHand.add_card(Card("Hearts", "Jack"))
        self.assertEqual(4, playersHand.value)

    def test_hand_value3(self):
        playersHand = Hand()
        playersHand.add_card(Card("Spades", "Two"))
        playersHand.add_card(Card("Hearts", "Two"))
        playersHand.add_card(Card("Diamonds", "Two"))
        playersHand.add_card(Card("Clubs", "Two"))
        self.assertEqual(8, playersHand.value)

    def test_hand_value4(self):
        playersHand = Hand()
        playersHand.add_card(Card("Spades", "Nine"))
        playersHand.add_card(Card("Hearts", "Nine"))
        playersHand.add_card(Card("Diamonds", "Nine"))
        self.assertEqual(27, playersHand.value)

    def test_hand_ace1(self):
        playersHand = Hand()
        playersHand.add_card(Card("Clubs", "King"))
        playersHand.add_card(Card("Spades", "King"))
        playersHand.add_card(Card("Clubs", "Ace"))
        self.assertEqual(17, playersHand.value)

    def test_hand_ace2(self):
        playersHand = Hand()
        playersHand.add_card(Card("Clubs", "King"))
        playersHand.add_card(Card("Hearts", "Ace"))
        self.assertEqual(14, playersHand.value)

    def test_hand_ace3(self):
        playersHand = Hand()
        playersHand.add_card(Card("Clubs", "Ten"))
        playersHand.add_card(Card("Spades", "Ten"))
        playersHand.add_card(Card("Clubs", "Ace"))
        self.assertEqual(31, playersHand.value)
        playersHand.adjust_for_ace()
        self.assertEqual(21, playersHand.value)

    def test_hand_isDealer1(self):
        out = io.StringIO()
        sys.stdout = out
        playersHand = Hand()
        playersHand.add_card(Card("Clubs", "Ten"))
        playersHand.add_card(Card("Spades", "Ten"))
        dealersHand = Hand()
        dealersHand.add_card(Card("Spades", "Eight"))
        dealersHand.add_card(Card("Diamonds", "Two"))
        show_some(playersHand,dealersHand)
        output = out.getvalue().strip()
        self.assertIn("<card hidden>", output)
        self.assertNotIn("Eight of Spades", output)

    def test_hand_isPlayer1(self):
        out = io.StringIO()
        sys.stdout = out
        playersHand = Hand()
        playersHand.add_card(Card("Clubs", "King"))
        playersHand.add_card(Card("Hearts", "Ace"))
        dealersHand = Hand()
        dealersHand.add_card(Card("Spades", "Eight"))
        dealersHand.add_card(Card("Diamonds", "Two"))
        show_some(playersHand,dealersHand)
        output = out.getvalue().strip()
        self.assertIn("King of Clubs", output)
        self.assertIn("Ace of Hearts", output)

    def test_chips_winBet(self):
        chips = Chips()
        chips.bet = 20
        chips.win_bet()
        self.assertEqual(120,chips.total)

    def test_chips_loseBet(self):
        chips = Chips()
        chips.bet = 20
        chips.lose_bet()
        self.assertEqual(80,chips.total)

if __name__ == '__main__':
    unittest.main()
