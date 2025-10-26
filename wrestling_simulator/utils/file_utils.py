"""
File utility functions for the Wrestling Simulator.
"""

import os
from typing import List


def get_data_path() -> str:
    """Get the path to the data directory."""
    return os.path.join(os.path.dirname(__file__), "..", "data")


def load_wrestler_names(gender: str) -> List[str]:
    """
    Load wrestler names from the appropriate built-in data file.

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

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Wrestler names file not found: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]

    if not names:
        raise ValueError(f"No valid wrestler names found in {filepath}")

    return names


def load_wrestler_names_from_file(path: str) -> List[str]:
    """
    Load wrestler names from a user-supplied text file.

    Args:
        path: Path to the text file containing wrestler names (one per line)

    Returns:
        List of wrestler names

    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file is empty or contains no valid names
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]

    if not names:
        raise ValueError("No valid wrestler names found in the file.")

    return names
