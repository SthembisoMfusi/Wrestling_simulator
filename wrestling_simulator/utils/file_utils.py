"""
File utility functions for the wrestling simulator.
"""

import os
from typing import List


def get_data_path() -> str:
    """Get the path to the data directory."""
    return os.path.join(os.path.dirname(__file__), "..", "data")


def load_wrestler_names(gender: str) -> List[str]:
    """
    Load wrestler names from the appropriate file.
    
    Args:
        gender: The gender of wrestlers ('male', 'female', or 'other')
        
    Returns:
        List of wrestler names
        
    Raises:
        ValueError: If gender is invalid
        FileNotFoundError: If the name file doesn't exist
    """
    valid_genders = ["male", "female", "other"]
    if gender.lower() not in valid_genders:
        raise ValueError(f"Gender must be one of {valid_genders}")
    
    data_path = get_data_path()
    filename = f"{gender.capitalize()} wrestlers.txt"
    filepath = os.path.join(data_path, "wrestler_names", filename)
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            names = [line.strip() for line in f if line.strip()]
        return names
    except FileNotFoundError:
        raise FileNotFoundError(f"Wrestler names file not found: {filepath}")
