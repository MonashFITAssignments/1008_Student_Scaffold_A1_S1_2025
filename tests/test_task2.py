from unittest import TestCase

from ed_utils.decorators import number, visibility
from data_structures import ArrayList

from game_board import GameBoard
from random_gen import RandomGen
from card import Card, CardColor, CardLabel
from player import Player
from constants import Constants


class TestGame(TestCase):

    def setUp(self) -> None:
        self.three_cards: ArrayList[Card] = ArrayList(3)
        self.three_cards.insert(0, Card(CardColor.BLUE, CardLabel.FIVE))
        self.three_cards.insert(1, Card(CardColor.RED, CardLabel.THREE))
        self.three_cards.insert(2, Card(CardColor.RED, CardLabel.FIVE))

    @number("2.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_game_board_init(self):
        game_board: GameBoard = GameBoard(self.three_cards)
        self.assertTrue(
            hasattr(game_board, "draw_pile"),
            f"draw_pile not found in GameBoard, please ensure your spelling is correct",
        )
        self.assertTrue(
            hasattr(game_board, "discard_pile"),
            f"discard_pile not found in GameBoard, please ensure your spelling is correct",
        )
        self.assertEqual(len(game_board.draw_pile), 3)
        self.assertEqual(len(game_board.discard_pile), 0)

    @number("2.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_discard_card(self) -> None:
        game_board: GameBoard = GameBoard(self.three_cards)
        self.assertEqual(len(game_board.discard_pile), 0)

        card: Card = Card(CardColor.BLUE, CardLabel.SEVEN)
        game_board.discard_card(card)
        self.assertEqual(
            len(game_board.discard_pile),
            1,
            f"There should be one card in the discard pile, but there are {len(game_board.draw_pile)}",
        )
        self.assertEqual(
            game_board.discard_pile.array[0].color,
            card.color,
            f"First card in discard pile should be BLUE, but is {game_board.discard_pile.array[0].color}",
        )
        self.assertEqual(
            game_board.discard_pile.array[0].label,
            card.label,
            f"First card in unused pile should be SEVEN, but is {game_board.discard_pile.array[0].label}",
        )

    @number("2.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_reshuffle(self) -> None:
        RandomGen.set_seed(5678)
        cards = ArrayList(1)
        cards.insert(0, Card(CardColor.BLUE, CardLabel.FIVE))

        game_board: GameBoard = GameBoard(cards)
        self.assertEqual(len(game_board.discard_pile), 0)

        game_board.discard_card(Card(CardColor.RED, CardLabel.SEVEN))
        game_board.discard_card(Card(CardColor.YELLOW, CardLabel.FOUR))
        self.assertEqual(len(game_board.discard_pile), 2)

        game_board.reshuffle()
        self.assertEqual(len(game_board.draw_pile), 3)
        self.assertEqual(len(game_board.discard_pile), 0)

        self.assertEqual(
            game_board.draw_pile.array[0].color,
            CardColor.BLUE,
            f"First card in draw pile should be BLUE, but is {game_board.draw_pile.array[0].color}",
        )
        self.assertEqual(
            game_board.draw_pile.array[0].label,
            CardLabel.FIVE,
            f"First card in draw pile should be FIVE, but is {game_board.draw_pile.array[0].label}",
        )
        self.assertEqual(
            game_board.draw_pile.array[1].color,
            CardColor.YELLOW,
            f"Second card in draw pile should be YELLOW, but is {game_board.draw_pile.array[1].color}",
        )
        self.assertEqual(
            game_board.draw_pile.array[1].label,
            CardLabel.FOUR,
            f"Second card in draw pile should be FOUR, but is {game_board.draw_pile.array[1].label}",
        )
        self.assertEqual(
            game_board.draw_pile.array[2].color,
            CardColor.RED,
            f"Second card in draw pile should be RED, but is {game_board.draw_pile.array[2].color}",
        )
        self.assertEqual(
            game_board.draw_pile.array[2].label,
            CardLabel.SEVEN,
            f"Second card in draw pile should be SEVEN, but is {game_board.draw_pile.array[2].label}",
        )

    @number("2.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_draw_card(self) -> None:
        game_board: GameBoard = GameBoard(self.three_cards)
        self.assertEqual(len(game_board.discard_pile), 0)
        self.assertEqual(len(game_board.draw_pile), 3)
        card = game_board.draw_card()
        self.assertEqual(
            card.color,
            CardColor.BLUE,
            f"First card drawn should be BLUE, but is {card.color}",
        )
        self.assertEqual(
            card.label,
            CardLabel.FIVE,
            f"First card drawn should be FIVE, but is {card.label}",
        )
        card = game_board.draw_card()
        self.assertEqual(
            card.color,
            CardColor.RED,
            f"First card drawn should be RED, but is {card.color}",
        )
        self.assertEqual(
            card.label,
            CardLabel.THREE,
            f"First card drawn should be THREE, but is {card.label}",
        )
        card = game_board.draw_card()
        self.assertEqual(
            card.color,
            CardColor.RED,
            f"Third card drawn should be RED, but is {card.color}",
        )
        self.assertEqual(
            card.label,
            CardLabel.FIVE,
            f"Third card drawn should be FIVE, but is {card.label}",
        )
