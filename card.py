from __future__ import annotations
from enum import auto, IntEnum
from constants import Constants
from data_structures import *


class CardColor(IntEnum):
    """
    Enum class for the color of the card
    """


    RED = 0
    BLUE = auto()
    GREEN = auto()
    YELLOW = auto()
    CRAZY = auto()



class CardLabel(IntEnum):
    """
    Enum class for the value of the card
    """


    ZERO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    SKIP = auto()
    REVERSE = auto()
    DRAW_TWO = auto()
    CRAZY = auto()
    DRAW_FOUR = auto()



class Card:
    def __init__(self, color: CardColor, label: CardLabel) -> None:
        """
        Initialize the card with the given color and value.

        Args:
            color (CardColor): The color of the card.
            value (CardValue): The value of the card.

        Returns:
            None

        Complexity:
            Best Case: 
            Worst Case: 
        """
        raise NotImplementedError
