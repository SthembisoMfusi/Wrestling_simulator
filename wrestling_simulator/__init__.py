"""
Wrestling Simulator - A Python-based wrestling tournament simulation game.

This package provides a complete wrestling simulation system with customizable
wrestlers, roster management, and tournament functionality.
"""

__version__ = "1.0.0"
__author__ = "Sthembiso Mfusi"
__email__ = "sthembiso.mfusi@example.com"

from .core.wrestler import Wrestler
from .core.roster import Roster
from .core.tournament import Tournament

__all__ = ["Wrestler", "Roster", "Tournament"]
