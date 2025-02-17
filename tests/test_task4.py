from unittest import TestCase

from ed_utils.decorators import number, visibility
from data_structures.referential_array import ArrayR

from game import Game
from random_gen import RandomGen
from card import CardColor, CardLabel
from player import Player
from constants import Constants


class TestTask4(TestCase):

    @number("4.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_small_game(self) -> None:
        # Set up the small game
        RandomGen.set_seed(123)
        Constants.NUM_CARDS_AT_INIT = 2
        players: ArrayR[Player] = ArrayR(4)
        a = Player("Alice")
        b = Player("Bob")
        c = Player("Charlie")
        d = Player("David")
        players[0] = a
        players[1] = b
        players[2] = c
        players[3] = d
        game: Game = Game()
        game.initialise_game(players)

        # Check the top card of the discard pile
        self.assertEqual(
            game.current_color,
            CardColor.GREEN,
            f"First card in discard pile should be GREEN, but is {game.current_color}",
        )
        self.assertEqual(
            game.current_label,
            CardLabel.TWO,
            f"First card in discard pile should be TWO, but is {game.current_label}",
        )

        # Play the game
        winner: Player = game.play_game()

        # Check the winner
        self.assertEqual(
            winner.name, c.name, f"Winner should be Charlie, but is {winner.name}"
        )

        # Check the leftover hand of Alice
        self.assertEqual(
            a.cards_at_hand(),
            3,
            f"Alice should have 3 cards left, but has {a.cards_at_hand()}",
        )

        # Check the leftover hand of Bob
        self.assertEqual(
            b.cards_at_hand(),
            3,
            f"Bob should have 3 cards left, but has {b.cards_at_hand()}",
        )

        # Check the leftover hand of David
        self.assertEqual(
            d.cards_at_hand(),
            1,
            f"David should have 1 cards left, but has {d.cards_at_hand()}",
        )

    @number("4.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_long_game(self) -> None:
        # Set up the long game
        RandomGen.set_seed(123)
        Constants.NUM_CARDS_AT_INIT = 7

        players: ArrayR[Player] = ArrayR(3)
        a = Player("Alice")
        b = Player("Bob")
        c = Player("Charlie")

        players[0] = a
        players[1] = b
        players[2] = c
        game: Game = Game()
        game.initialise_game(players)

        # Check the top card of the discard pile
        self.assertEqual(
            game.current_color,
            CardColor.GREEN,
            f"First card in discard pile should be GREEN, but is {game.current_color}",
        )
        self.assertEqual(
            game.current_label,
            CardLabel.THREE,
            f"First card in discard pile should be THREE, but is {game.current_label}",
        )

        # Play the game
        winner: Player = game.play_game()

        # Check the winner
        self.assertEqual(
            winner.name, a.name, f"Winner should be Alice, but is {winner.name}"
        )

        # Check the leftover hand of Bob
        self.assertEqual(
            b.cards_at_hand(),
            3,
            f"Bob should have 3 cards left, but has {b.cards_at_hand()}",
        )

        # Check the leftover hand of Charlie
        self.assertEqual(
            c.cards_at_hand(),
            6,
            f"Charlie should have 6 cards left, but has {c.cards_at_hand()}",
        )
