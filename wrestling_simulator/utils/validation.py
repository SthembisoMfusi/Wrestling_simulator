"""
Validation utility functions for the wrestling simulator.
"""

from typing import Dict, Any, Callable, Tuple


def validate_wrestler_stats(stats: Dict[str, Any]) -> None:
    """
    Validate wrestler statistics.

    Args:
        stats: Dictionary containing wrestler stats

    Raises:
        ValueError: If any stat is invalid
    """
    validations: Dict[str, Tuple[Callable[[Any], bool], str]] = {
        "name": (
            lambda x: isinstance(x, str),
            "Name must be a string (e.g., 'The Rock' or 'Stone Cold')",
        ),
        "gender": (
            lambda x: x in ["male", "female", "other"],
            "Gender must be 'male', 'female', or 'other'",
        ),
        "strength": (
            lambda x: isinstance(x, int) and 40 <= x <= 100,
            "Strength must be between 40-100 (determines damage resistance, try 70 or 85)",
        ),
        "speed": (
            lambda x: isinstance(x, int) and 30 <= x <= 100,
            "Speed must be between 30-100 (affects attack speed, try 65 or 80)",
        ),
        "agility": (
            lambda x: isinstance(x, int) and 10 <= x <= 100,
            "Agility must be between 10-100 (helps escape moves, try 50 or 75)",
        ),
        "health": (
            lambda x: isinstance(x, int) and 80 <= x <= 200,
            "Health must be between 80-200 (total damage capacity, try 120 or 160)",
        ),
        "power": (
            lambda x: isinstance(x, int) and 50 <= x <= 100,
            "Power must be between 50-100 (attack damage output, try 75 or 90)",
        ),
        "grapple": (
            lambda x: isinstance(x, int) and 1 <= x <= 20,
            "Grapple must be between 1-20 (grappling success rate, try 10 or 15)",
        ),
        "stamina": (
            lambda x: isinstance(x, int) and 30 <= x <= 100,
            "Stamina must be between 30-100 (special move frequency, try 60 or 80)",
        ),
    }

    for stat_name, (validator, error_msg) in validations.items():
        if stat_name in stats:
            if not validator(stats[stat_name]):
                actual_value = stats[stat_name]
                raise ValueError(f"Invalid {stat_name}: {actual_value}. {error_msg}")


def validate_tournament_size(size: int) -> None:
    """
    Validate tournament size.

    Args:
        size: Number of participants

    Raises:
        ValueError: If tournament size is invalid
    """
    if not isinstance(size, int):
        raise ValueError(
            f"Invalid tournament size type: {type(size).__name__}. "
            f"Tournament size must be an integer. Try 4, 8, 16, or 32."
        )

    if size < 4:
        raise ValueError(
            f"Tournament size too small: {size}. "
            f"Tournament must have at least 4 participants. Try 4, 8, or 16."
        )

    if size % 2 != 0:
        raise ValueError(
            f"Invalid tournament size: {size}. "
            f"Tournament size must be even (divisible by 2). Try {size - 1} or {size + 1}."
        )

    # Check if it's a power of 2 (optional but common for tournaments)
    if size & (size - 1) != 0:
        # Find nearest power of 2
        import math

        lower = 2 ** math.floor(math.log2(size))
        upper = 2 ** math.ceil(math.log2(size))
        raise ValueError(
            f"Invalid tournament size: {size}. "
            f"Tournament size should be a power of 2 for proper bracket structure. "
            f"Try {lower} or {upper} participants instead."
        )
