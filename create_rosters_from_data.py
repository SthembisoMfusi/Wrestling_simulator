#!/usr/bin/env python3
"""
Script to create roster files using wrestler names from the data folder.
"""

import os
import sys
import random
from pathlib import Path

# Add current directory to path
sys.path.insert(0, ".")

from wrestling_simulator import Roster, Wrestler


def load_wrestler_names(file_path):
    """Load wrestler names from a text file."""
    names = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                name = line.strip()
                if name and not name.startswith("#"):  # Skip empty lines and comments
                    names.append(name)
    except FileNotFoundError:
        print(f"Warning: Could not find {file_path}")
    return names


def create_roster_from_names(name, wrestler_names, gender, count=8):
    """Create a roster with wrestlers from the given name list."""
    roster = Roster(auto_fill=False)
    roster.roster = []

    selected_names = random.sample(wrestler_names, min(count, len(wrestler_names)))

    for name in selected_names:
        strength = random.randint(50, 100)
        power = random.randint(50, 100)
        speed = random.randint(30, 100)
        health = random.randint(100, 200)
        stamina = random.randint(50, 100)
        grapple = random.randint(1, 20)

        agility = random.randint(10, 100)

        wrestler = Wrestler(
            name=name,
            gender=gender,
            strength=strength,
            power=power,
            speed=speed,
            agility=agility,
            health=health,
            stamina=stamina,
            grapple=grapple,
        )
        roster.roster.append(wrestler)

    return roster


def main():
    """Create various roster files using the data folder names."""
    print("Creating roster files from wrestler name data...")

    # Ensure rosters directory exists
    rosters_dir = "rosters"
    if not os.path.exists(rosters_dir):
        os.makedirs(rosters_dir)

    # Load wrestler names from data files
    data_dir = "wrestling_simulator/data/wrestler_names"

    male_names = load_wrestler_names(os.path.join(data_dir, "Male wrestlers.txt"))
    female_names = load_wrestler_names(os.path.join(data_dir, "Female wrestlers.txt"))
    other_names = load_wrestler_names(os.path.join(data_dir, "Other wrestlers.txt"))

    print(f"Loaded {len(male_names)} male wrestler names")
    print(f"Loaded {len(female_names)} female wrestler names")
    print(f"Loaded {len(other_names)} other wrestler names")

    # Create various roster types
    rosters_to_create = [
        # (filename, description, names, gender, count)
        (
            "legendary_male_roster.pickle",
            "Legendary Male Wrestlers",
            male_names,
            "male",
            8,
        ),
        (
            "legendary_female_roster.pickle",
            "Legendary Female Wrestlers",
            female_names,
            "female",
            8,
        ),
        (
            "mixed_legends_roster.pickle",
            "Mixed Legendary Wrestlers",
            male_names + female_names,
            "mixed",
            12,
        ),
        ("modern_male_roster.pickle", "Modern Male Wrestlers", male_names, "male", 6),
        (
            "modern_female_roster.pickle",
            "Modern Female Wrestlers",
            female_names,
            "female",
            6,
        ),
        (
            "diverse_roster.pickle",
            "Diverse Wrestlers",
            male_names + female_names + other_names,
            "mixed",
            10,
        ),
        ("tag_team_roster.pickle", "Tag Team Specialists", male_names, "male", 4),
        ("women_division_roster.pickle", "Women's Division", female_names, "female", 8),
        ("indie_roster.pickle", "Independent Wrestlers", other_names, "mixed", 6),
        (
            "hall_of_fame_roster.pickle",
            "Hall of Fame",
            male_names + female_names,
            "mixed",
            16,
        ),
    ]

    created_rosters = []

    for filename, description, names, gender, count in rosters_to_create:
        if len(names) < count:
            print(
                f"Warning: Not enough names in {description} ({len(names)} available, {count} requested)"
            )
            count = len(names)

        if count == 0:
            print(f"Skipping {description} - no names available")
            continue

        print(f"Creating {description} ({count} wrestlers)...")
        roster = create_roster_from_names(description, names, gender, count)

        # Save the roster
        filepath = os.path.join(rosters_dir, filename)
        roster.save_roster(filename)
        created_rosters.append((filename, description, len(roster.roster)))

        print(f"  ✓ Saved {filename} with {len(roster.roster)} wrestlers")

    # Display summary
    print("\n" + "=" * 60)
    print("ROSTER CREATION SUMMARY")
    print("=" * 60)

    for filename, description, count in created_rosters:
        print(f"📁 {filename:<30} | {description:<25} | {count:>2} wrestlers")

    print(f"\nTotal rosters created: {len(created_rosters)}")
    print(f"All rosters saved to: {rosters_dir}/")

    # Test the new roster listing functionality
    print("\n" + "=" * 60)
    print("TESTING NEW ROSTER LISTING FEATURE")
    print("=" * 60)

    available_rosters = Roster.list_available_rosters()
    print("Available rosters with wrestler counts:")
    for i, (roster_file, wrestler_count) in enumerate(available_rosters, 1):
        print(f"{i:>2}. {roster_file:<30} ({wrestler_count:>2} wrestlers)")

    print(f"\nTotal rosters available: {len(available_rosters)}")


if __name__ == "__main__":
    main()
