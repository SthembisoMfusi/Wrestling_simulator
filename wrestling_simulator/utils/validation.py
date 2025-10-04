"""
Validation utility functions for the wrestling simulator.
"""

from typing import Dict, Any


def validate_wrestler_stats(stats: Dict[str, Any]) -> None:
    """
    Validate wrestler statistics.
    
    Args:
        stats: Dictionary containing wrestler stats
        
    Raises:
        ValueError: If any stat is invalid
    """
    validations = {
        "name": (str, "Name must be a string"),
        "gender": (lambda x: x in ["male", "female", "other"], "Gender must be 'male', 'female', or 'other'"),
        "strength": (lambda x: isinstance(x, int) and 40 <= x <= 100, "Strength must be between 40 and 100"),
        "speed": (lambda x: isinstance(x, int) and 30 <= x <= 100, "Speed must be between 30 and 100"),
        "agility": (lambda x: isinstance(x, int) and 10 <= x <= 100, "Agility must be between 10 and 100"),
        "health": (lambda x: isinstance(x, int) and 80 <= x <= 200, "Health must be between 80 and 200"),
        "power": (lambda x: isinstance(x, int) and 50 <= x <= 100, "Power must be between 50 and 100"),
        "grapple": (lambda x: isinstance(x, int) and 1 <= x <= 20, "Grapple must be between 1 and 20"),
        "stamina": (lambda x: isinstance(x, int) and 30 <= x <= 100, "Stamina must be between 30 and 100"),
    }
    
    for stat_name, (validator, error_msg) in validations.items():
        if stat_name in stats:
            if not validator(stats[stat_name]):
                raise ValueError(f"{stat_name.capitalize()}: {error_msg}")


def validate_tournament_size(size: int) -> None:
    """
    Validate tournament size.
    
    Args:
        size: Number of participants
        
    Raises:
        ValueError: If tournament size is invalid
    """
    if not isinstance(size, int):
        raise ValueError("Tournament size must be an integer")
    
    if size < 4:
        raise ValueError("Tournament must have at least 4 participants")
    
    if size % 2 != 0:
        raise ValueError("Tournament size must be even (divisible by 2)")
    
    # Check if it's a power of 2 (optional but common for tournaments)
    if size & (size - 1) != 0:
        raise ValueError("Tournament size should be a power of 2 (4, 8, 16, 32, etc.)")
